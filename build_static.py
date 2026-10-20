"""Render the Flask portfolio to a validated, portable GitHub Pages site."""
import os
import re
import shutil
import posixpath
from pathlib import Path
from urllib.parse import urlsplit
from xml.sax.saxutils import escape

from app import create_app
from app.services.portfolio_service import get_portfolio_data
from app.services.presentation import SITE_URL


def fix_urls_for_static_site(content, filename, portfolio_data):
    routes = {'/': 'index.html', '/hobby': 'hobby.html', '/archive': 'hobby.html',
              '/narrative/nexus': 'narrative_nexus.html', '/narrative/': 'narrative_nexus.html',
              '/chat/bot': 'chatbot.html', '/chat/': 'chatbot.html'}
    routes.update({f'/project/{p.id}': f'project/{p.id}.html' for p in portfolio_data.projects})
    folder = posixpath.dirname(filename) or '.'

    def rewrite(match):
        attr, quote, raw = match.groups()
        if not raw.startswith('/') or raw.startswith('//'):
            return match.group(0)
        url = urlsplit(raw)
        target = routes.get(url.path)
        if url.path.startswith('/static/'):
            target = url.path.lstrip('/')
        if not target:
            return match.group(0)
        # 404.html can be served at any depth on GitHub Pages.
        if filename == '404.html':
            result = urlsplit(SITE_URL).path + '/' + target
        else:
            result = posixpath.relpath(target, folder)
            if not result.startswith('.'):
                result = './' + result
        if url.query:
            result += '?' + url.query
        if url.fragment:
            result += '#' + ('experience' if url.fragment == 'about' else url.fragment)
        return f'{attr}={quote}{result}{quote}'

    return re.sub(r'\b(href|src|action|data-action|data-project-llm|data-project-reasoning|data-project-agents)=([\"\'])(.*?)\2', rewrite, content).replace('index.html#about', 'index.html#experience')


def build_static_site():
    os.environ.setdefault('SECRET_KEY', 'static-build-key')
    from build_cv import build_cv
    build_cv()
    output = Path('dist')
    if output.exists():
        shutil.rmtree(output)
    output.mkdir()
    shutil.copytree('app/static', output / 'static')
    app = create_app('production')
    app.config['TESTING'] = True
    portfolio = get_portfolio_data()
    routes = [('/', 'index.html'), ('/hobby', 'hobby.html'),
              ('/narrative/nexus', 'narrative_nexus.html'), ('/chat/bot', 'chatbot.html')]
    routes += [(f'/project/{p.id}', f'project/{p.id}.html') for p in portfolio.projects]
    routes.append(('/__not_found__', '404.html'))
    with app.test_client() as client:
        for route, filename in routes:
            response = client.get(route)
            expected = 404 if filename == '404.html' else 200
            if response.status_code != expected:
                raise RuntimeError(f'{route}: expected {expected}, got {response.status_code}')
            html = fix_urls_for_static_site(response.get_data(as_text=True), filename, portfolio)
            target = output / filename
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text('\n'.join(line.rstrip() for line in html.splitlines()) + '\n', encoding='utf-8')
            print(f'Built {filename}')
    # Preserve this previously public standalone essay page.
    if Path('blogs.html').exists():
        html = fix_urls_for_static_site(Path('blogs.html').read_text(), 'blogs.html', portfolio)
        (output / 'blogs.html').write_text('\n'.join(line.rstrip() for line in html.splitlines()) + '\n', encoding='utf-8')
    (output / '.nojekyll').touch()
    (output / 'robots.txt').write_text(f'User-agent: *\nAllow: /\nSitemap: {SITE_URL}/sitemap.xml\n')
    urls = [SITE_URL + '/' + name for _, name in routes if name not in {'404.html', 'chatbot.html'}]
    entries = ''.join(f'<url><loc>{escape(url)}</loc></url>' for url in urls)
    (output / 'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' + entries + '</urlset>')
    print(f'Built {len(routes)} pages in dist/')


if __name__ == '__main__':
    build_static_site()
