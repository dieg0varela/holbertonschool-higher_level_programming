#!/usr/bin/python3
'''Task 2 Module'''
import urllib.parse
import urllib.request
import sys
if __name__ == "__main__":
    data = urllib.parse.urlencode({"email": sys.argv[2]}).encode()
    req = urllib.request.Request(sys.argv[1], data=data)
    with urllib.request.urlopen(req) as response:
        html = response.read()
        print(html.decode('utf-8'))
