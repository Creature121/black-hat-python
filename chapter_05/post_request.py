import urllib.parse
import urllib.request

url = "https://www.nostarch.com"
info = {"user": "tim", "passwd": "31337"}
data = urllib.parse.urlencode(info).encode()

request = urllib.request.Request(url, data)

with urllib.request.urlopen(request) as response:
    content = response.read()

print(content)
