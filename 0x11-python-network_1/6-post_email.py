#!/usr/bin/python3
'''Task 6 Module'''
import requests
from sys import argv
if __name__ == "__main__":
    response = requests.post(argv[1], data={'email': argv[2]})
    print(response.text)
