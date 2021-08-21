#!/usr/bin/python3
'''Task 8 Module'''
import requests
from sys import argv
if __name__ == "__main__":
    if len(argv) == 2:
        q = argv[1]
    else:
        q = ""
    response = requests.post("http://0.0.0.0:5000/search_user", data={"q": q})
    if (type(response.json()) == dict):
        if (len(response.json()) > 0):
            id = response.json().get("id")
            name = response.json().get("name")
            print("[{}] {}".format(id, name))
        else:
            print("No result")
    else:
        print("Not a valid JSON")
