#!/usr/bin/python3
'''Task 3 Module'''
import urllib.parse
import urllib.request
import sys
if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            html = response.read()
            print(html.decode('utf-8'))
    except urllib.error.HTTPError as exception:
        print("Error code: {}".format(exception.code))
