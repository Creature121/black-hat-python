import requests

url = "https://www.nostarch.com"
get_response = requests.get(url)

data = {"user": "tim", "passwd": "31337"}
post_response = requests.post(url, data)

print(get_response.text)
print(post_response.text)
