import http.server
import socketserver
PORT = 8000
handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("",PORT),handler) as sock:
    sock.serve_forever()