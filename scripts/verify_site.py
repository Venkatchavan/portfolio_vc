"""Check the actual deployment artifact, not just the Flask source routes."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote
import re
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parent.parent / 'dist'
BASE = '/portfolio_vc/'

class Page(HTMLParser):
    def __init__(self, source):
        super().__init__(convert_charrefs=True)
        self.links, self.ids, self.headings, self.images = [], set(), [], []
        self.feed(source)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            self.ids.add(attrs['id'])
        if tag in ('h1', 'h2', 'h3', 'h4', 'h5', 'h6'):
            self.headings.append(int(tag[1]))
        if tag in ('a', 'link', 'script', 'img'):
            url = attrs.get('href') or attrs.get('src')
            if url:
                self.links.append(url)
        if tag == 'img':
            self.images.append(attrs)


def main():
    pages = {p.resolve(): Page(p.read_text(encoding='utf-8')) for p in ROOT.rglob('*.html')}
    errors = []
    for path, page in pages.items():
        source = path.read_text()
        label = str(path.relative_to(ROOT))
        if '{{' in source or '{%' in source:
            errors.append(f'{label}: unrendered template')
        if page.headings.count(1) != 1:
            errors.append(f'{label}: expected one h1')
        if any('alt' not in img for img in page.images):
            errors.append(f'{label}: missing image alt')
        for href in page.links:
            url = urlsplit(href)
            if url.scheme or url.netloc or href == '#':
                continue
            raw = unquote(url.path)
            if raw.startswith(BASE):
                target = ROOT / raw[len(BASE):]
            elif raw.startswith('/'):
                target = ROOT / raw.lstrip('/')
            else:
                target = path.parent / raw if raw else path
            target = target.resolve()
            if target.is_dir():
                target /= 'index.html'
            if not target.exists():
                errors.append(f'{label}: missing local link {href}')
            elif url.fragment and target in pages and unquote(url.fragment) not in pages[target].ids:
                errors.append(f'{label}: missing anchor {href}')
    for path in (ROOT / 'static/css').glob('*.css'):
        for href in re.findall(r'url\([\'\"]?([^\)\'\"]+)', path.read_text()):
            if href.startswith(('http:', 'https:', 'data:', '#')):
                continue
            if not (path.parent / href).exists():
                errors.append(f'{path.name}: missing CSS asset {href}')
    for name in ('robots.txt', 'sitemap.xml', '404.html', '.nojekyll', 'static/images/og.png'):
        if not (ROOT / name).exists():
            errors.append(f'Missing deployment file {name}')
    if (ROOT / 'sitemap.xml').exists():
        ET.parse(ROOT / 'sitemap.xml')
    home = (ROOT / 'index.html').read_text()
    for fact in ('93.5', '88.7', '6.8', '6.5%', '11.3%', 'Preprint forthcoming'):
        if fact not in home:
            errors.append(f'Study context missing: {fact}')
    if errors:
        raise SystemExit('\n'.join(errors))
    print(f'PASS: {len(pages)} HTML pages, local links and anchors, CSS assets, chart context and deployment files.')

if __name__ == '__main__':
    main()
