#!/usr/bin/python3
import sys
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

FILENAME = "add_item.json"

try:
    items = load_from_json_file(FILENAME)
except FileNotFoundError:
    items = []

items += sys.argv[1:]
save_to_json_file(items, FILENAME)
