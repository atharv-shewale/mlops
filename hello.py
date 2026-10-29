"""
Single-file Lightweight Application for MLOps UAT Deployment
Supports both CLI verification and HTTP deployment using Python standard library.
"""

import sys
import time
from http.server import HTTPServer, BaseHTTPRequestHandler

HOST = "0.0.0.0"
PORT = 8000

def get_message(name: str = "World") -> str:
    return f"Hello, {name}! Welcome to MLOps UAT Environment."

class UATHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        message = get_message("DevOps Team")
        response_body = (
            f"==================================================\n"
            f"{message}\n"
            f"Application Status: RUNNING (OK) - DEPLOYED ON DOCKER\n"
            f"Port: {PORT}\n"
            f"Timestamp: {time.strftime('%Y-%m-%d %H:%M:%S')}\n"
            f"==================================================\n"
        ).encode("utf-8")
        
        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", str(len(response_body)))
        self.end_headers()
        self.wfile.write(response_body)

    def log_message(self, format, *args):
        print(f"[HTTP SERVER] {self.address_string()} - {format % args}")

def run_server():
    server = HTTPServer((HOST, PORT), UATHandler)
    print("=" * 50)
    print(get_message("DevOps Team"))
    print(f"Application Status: RUNNING (OK)")
    print(f"Deployment Target: Docker Container on http://{HOST}:{PORT}")
    print("=" * 50)
    server.serve_forever()

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--serve":
        run_server()
    else:
        # Default CLI print execution
        print("=" * 50)
        print(get_message("DevOps Team"))
        print("Application Status: RUNNING (OK)")
        print("=" * 50)
