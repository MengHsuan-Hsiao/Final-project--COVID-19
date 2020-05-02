# For mac users
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

import urllib.request as req
url = "https://www.nytimes.com/interactive/2020/us/coronavirus-us-cases.html"

# Create a Reqeust object with Request Headers 
# Mimic normal users
request = req.Request(url, headers={
	"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"
	})

with req.urlopen(request) as response:
	data = response.read()
# print(data)

import bs4
root = bs4.BeautifulSoup(data, "html.parser")
print(root.title.string)