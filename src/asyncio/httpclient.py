

import http.client

conn = http.client.HTTPSConnection("http://127.0.0.1:8000")
conn.request("GET", "/")
r1 = conn.getresponse()
print(r1.status, r1.reason)


