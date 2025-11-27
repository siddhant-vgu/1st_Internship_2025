import http.server
import socketserver  

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Server running at http://10.110.137.1:8000")
    httpd.serve_forever()