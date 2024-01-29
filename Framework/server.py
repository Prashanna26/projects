import http.server
from urllib.parse import parse_qs
from router import routes
from model import Model_data
import json
def get_handler(path):
    return routes.get(path, None)

class FrameworkHandler(http.server.SimpleHTTPRequestHandler):
    def do_HEAD(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_POST(self):
        if self.path == '/submit':
            content_len = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_len).decode("utf-8")
            json_data = json.loads(post_data)
            data = Model_data()
            data.add_item(json_data)

            self.do_GET()
            self.send_response(200) 
            self.send_header('Content-type', 'text/plain')
            self.end_headers()

        else:
            return super().do_POST()

        
    def do_GET(self):
        handler = get_handler(self.path)
        if handler:
            response = handler()
            self.do_HEAD()
            self.wfile.write(response)
        else:
            return http.server.SimpleHTTPRequestHandler.do_GET(self)
        
if __name__=='__main__':
    from http.server import HTTPServer

    host = 'localhost'
    port = 9001

    httpd = HTTPServer((host, port), FrameworkHandler)

    print(f"Starting server on http://{host}:{port}")

    httpd.serve_forever()
