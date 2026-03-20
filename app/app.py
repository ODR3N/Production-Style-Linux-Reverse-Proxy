from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import socket

HOST = "0.0.0.0"
PORT = 8080

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        message = f"""

Demo App Response
Time: {time.ctime()}
Hostname: {socket.gethostname()}
Client: {self.client_address[0]}
Path: {self.path}
"""
   

        self.send_response(200)
        self.send_header("Content-type", "test/plain")
        self.end_headers()
        self.wfile.write(message.encode())

server = HTTPServer((HOST, PORT), Handler)
print(f"Starting Server on {HOST}:{PORT}")
server.serve_forever()

