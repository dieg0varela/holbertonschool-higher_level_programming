#!/usr/bin/python3
'''Task 1 Module'''
import urllib.request
from sys import argv
if __name__ == "__main__":
    with urllib.request.urlopen(argv[1]) as response:
        html = response.read()
        print(response.info()["X-Request-Id"])
