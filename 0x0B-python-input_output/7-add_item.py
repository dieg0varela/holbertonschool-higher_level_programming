#!/usr/bin/python3
'''Load add and save Module'''


import json
from sys import argv
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file
size = len(argv) - 1
lista = []
try:
    lista = load_from_json_file("add_item.json")
except:
    lista = []
for i in range(size):
    lista.append(argv[i + 1])
save_to_json_file(lista, "add_item.json")
