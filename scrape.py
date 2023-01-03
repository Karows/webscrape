import requests
from bs4 import BeautifulSoup

url = "https://example.com"
res = requests.get(url)
soup = BeautifulSoup(res.content, "html.parser")
tag = soup.body

for string in tag.strings:
    print(string)
