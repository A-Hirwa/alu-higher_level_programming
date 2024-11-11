#!/usr/bin/python3
"""
7-add_item.py

This script adds all argumnent of a python list to a JSON file
"""


import json


save_to = __import__('5-save_to_json_file.py').save_to_json_file
load_fro = __import__('6-load_from_json_file.py').load_from_json_file


"""
This function loads the JSON file
"""
new_file = load_fro(add_item.json)
"""
This function saves the JSON file
"""
save_to(new_file)
