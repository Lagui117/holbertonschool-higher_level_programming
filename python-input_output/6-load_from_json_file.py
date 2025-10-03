#!/usr/bin/python3
"""Create a Python object from a JSON file."""
import json


def load_from_json_file(filename):
    """Load and return the Python object stored as JSON in `filename`."""
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)

