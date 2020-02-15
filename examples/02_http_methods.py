import json
from http.server import HTTPServer, BaseHTTPRequestHandler
from io import BytesIO


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        # -= Practice =-
        # Access your http server through your browser, do you get a "Hello world"?
        # Do a GET with Postman
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'{"message": "Hello, world!"}')


    def do_POST(self):
        # -= Assignment =-
        # Create a Post function and do a POST with Postman
        # Post your name and age and make the http server return it
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        self.send_response(200)
        self.end_headers()
        response = BytesIO()
        response.write(b'This is POST request. \n')
        response.write(b'\nReceived: ')
        response.write(body)
        self.wfile.write(response.getvalue())


# Start the HTTP Server
PORT = 8080

httpd = HTTPServer(('localhost', PORT), SimpleHTTPRequestHandler)
print("serving at port", PORT)
httpd.serve_forever()
