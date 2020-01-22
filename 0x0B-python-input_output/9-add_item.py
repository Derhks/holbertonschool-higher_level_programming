#!/usr/bin/python3


from sys import argv
from os import path

save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

if path.isfile("add_item.json"):
    new_list = load_from_json_file("add_item.json")
else:
    new_list = []

new_list += argv[1:]

save_to_json_file(new_list, "add_item.json")
