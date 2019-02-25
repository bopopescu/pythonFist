
# import json
# print(json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}]))
# print(json.dumps({"c": 0, "b": 0, "a": 0}, sort_keys=True))

# from io import StringIO

# io = StringIO()
# json.dump(['streaming API'], io)
# print(io.getvalue())

# import urllib.request
#
# with urllib.request.urlopen('http://www.python.org/') as f:
#     print(f.read(300))

# from urllib.parse import urlparse
# o = urlparse('http://www.cwi.nl:80/%7Eguido/Python.html')
# print(o)



import http.server
import socketserver

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("127.0.0.1", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()






































