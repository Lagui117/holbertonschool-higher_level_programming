#!/usr/bin/python3
"""Return a dictionary description for JSON serialization of an object."""


def class_to_json(obj):
    """Return a JSON-serializable dict of an object's attributes."""
    return obj.__dict__
