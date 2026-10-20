"""Serve the production build, including GitHub Pages base paths and real 404s."""
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlsplit

class PreviewHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(Path(__file__).resolve().parent.parent / 'dist'), **kwargs)

    def do_GET(self):
        if self.path.startswith('/portfolio_vc/'):
            self.path = self.path[len('/portfolio_vc'):]
        if not Path(self.translate_path(urlsplit(self.path).path)).exists():
            html = Path(self.directory, '404.html').read_bytes()
            self.send_response(404)
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.send_header('Content-Length', str(len(html)))
            self.end_headers()
            self.wfile.write(html)
            return
        super().do_GET()

if __name__ == '__main__':
    print('Production preview: http://127.0.0.1:4400/portfolio_vc/', flush=True)
    ThreadingHTTPServer(('127.0.0.1', 4400), PreviewHandler).serve_forever()
