from io import BytesIO  # allows a byte string to be used as a file object
from lxml import etree  # type: ignore
import requests

url = "https://nostarch.com"

r = requests.get(url)
content = r.content

parser = etree.HTMLParser()

content = etree.parse(BytesIO(content), parser=parser)

for link in content.findall("//a"):
    print(f"{link.get('href')} -> {link.text}")
