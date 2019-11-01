import BaseHTTPServer, SimpleHTTPServer
from urlparse import urlparse, parse_qs
from urllib import quote
form = """
<form action="" method="GET">
  <input id="query" name="query" value="Enter user name here..."
    onfocus="this.value=''">
  <input id="button" type="submit" value="Show my files">
</form><br>
"""
template = 'Files of %USERNAME%'

class ServerHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        #Show it later - and explain!
        self.send_header("X-XSS-Protection","0")
        self.end_headers()
        params = parse_qs(urlparse(self.path).query)
        print params
        username = ''
        if 'query' in params:
            username = params['query'][0].replace("script", "XSS").replace("SCRIPT", "XSS").replace("\"","&quot;").replace("\'","&quot;")
        res = template.replace('%USERNAME%', username)
        print "Returning res: " + form + res
        self.wfile.write(form + res)
        return

httpd = BaseHTTPServer.HTTPServer(('', 8080), ServerHandler)
httpd.serve_forever()