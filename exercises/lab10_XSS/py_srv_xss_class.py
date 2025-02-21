from http.server import HTTPServer, SimpleHTTPRequestHandler
from urllib.parse import urlparse, parse_qs, quote
import os

# HTML Form
form = """
<form action="" method="GET">
  <input id="query" name="query" value="Enter user name here..."
    onfocus="this.value=''">
  <input id="button" type="submit" value="Show my files">
</form><br>
"""

# HTML Template
template = '<a href="/directory/%USERNAME%">Files of %USERNAME%</a>'

# Custom Request Handler
class ServerHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.send_header("X-XSS-Protection", "0")  # Disabled for testing
        self.end_headers()
        
        params = parse_qs(urlparse(self.path).query)
        print(params)

        username = ''
        if 'query' in params:
            username = params['query'][0].replace("<", "&lt;").replace(">", "&gt;")

        res = template.replace('%USERNAME%', username)

        # Print for debugging
        print("Returning res: " + form + res)

        # Convert to bytes for writing
        self.wfile.write((form + res).encode('utf-8'))

# Run the HTTP Server
httpd = HTTPServer(('', 8080), ServerHandler)
print("Serving HTTP on port 8080...")
httpd.serve_forever()
