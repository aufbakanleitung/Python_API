import base64
from http.server import HTTPServer, BaseHTTPRequestHandler
from io import BytesIO
import argparse
import json

key = "dXNlcjpwYXNzd29yZA=="  # Hash of username "user" and password "password" in base64 encryption (user:password)
# print(base64.standard_b64encode("hi"))

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_AUTHHEAD(self):
        self.send_response(401)
        self.send_header(
            'WWW-Authenticate', 'Basic realm="Demo Realm"')
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_GET(self):
        print("self")
        print(self.headers)
        if self.headers.get('Authorization') is None:
            self.do_AUTHHEAD()

            response = {
                'success': False,
                'error': 'No auth header received'
            }

            self.wfile.write(bytes(json.dumps(response), 'utf-8'))

        elif self.headers.get('Authorization') == 'Basic ' + str(key):
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'{"message": "Hey mom, look: I\'m a protected Hello world!"}')

        else:
            self.do_AUTHHEAD()

            response = {
                'success': False,
                'error': 'Invalid credentials'
            }

            self.wfile.write(bytes(json.dumps(response), 'utf-8'))

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        self.send_response(200)
        self.end_headers()
        response = BytesIO()
        response.write(b'This is POST request. \n')
        response.write(b'\nReceived: ')
        response.write(body)
        self.wfile.write(response.getvalue())


def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, addr="localhost", port=8080):
    server_address = (addr, port)
    httpd = server_class(server_address, handler_class)

    print(f"Starting httpd server on {addr}:{port}")
    httpd.serve_forever()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run a simple HTTP server")
    parser.add_argument(
        "-l",
        "--listen",
        default="localhost",
        help="Specify the IP address on which the server listens",
    )
    parser.add_argument(
        "-p",
        "--port",
        type=int,
        default=8080,
        help="Specify the port on which the server listens",
    )
    args = parser.parse_args()
    run(addr=args.listen, port=args.port)


# -= Assignment =-
# Run this server and try to access it through Postman
