#!/usr/bin/python3
'''Task 4 Module'''
import requests
response = requests.get('https://intranet.hbtn.io/status')
html = response.text
print("Body response:")
print("	- type: {}".format(type(html)))
print("	- content: {}".format(html))
