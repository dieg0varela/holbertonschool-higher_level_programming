#!/usr/bin/python3
'''Task 2 Module'''
import urllib.request
import urllib.parse
from sys import argv
if __name__ == "__main__":
    data = urllib.parse.urlencode({"email":argv[2]})
    data = data.encode('ascii')
    with urllib.request.urlopen(argv[1], data) as response:
        html = response.read()
        print(html.decode())
