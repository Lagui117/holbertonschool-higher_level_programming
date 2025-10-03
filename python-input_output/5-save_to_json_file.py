#!/usr/bin/python3
"""Write a Python object to a file using its JSON representation."""
import json


def save_to_json_file(my_obj, filename):
    """Save `my_obj` to `filename` in JSON format (UTF-8)."""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
