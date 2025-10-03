#!/usr/bin/python3
def class_to_json(obj):
    """Return a dict description of obj suitable for JSON serialization."""
    return obj.__dict__
