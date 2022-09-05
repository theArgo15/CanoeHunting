import requests
url = 'https://www.elyoutdoor.com/site-content/canoe-rentals/canoes-for-sale'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"}
res = requests.get(url, headers = headers)
print(res.raise_for_status())
webFile = open('ElyOutdoor.html','wb')
for chunk in res.iter_content(100000):
    webFile.write(chunk)
webFile.close()