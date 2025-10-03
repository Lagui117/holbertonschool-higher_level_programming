#!/usr/bin/python3
"""Return the JSON string representation of a Python object."""
import json


def to_json_string(my_obj):
    """Return JSON string representation of `my_obj`."""
    return json.dumps(my_obj)
