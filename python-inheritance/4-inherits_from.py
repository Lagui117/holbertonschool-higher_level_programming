#!/usr/bin/python3
"""Check if an object is strictly instance of a subclass of a_class."""


def inherits_from(obj, a_class):
    """Return True if obj is an instance of a subclass of a_class."""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
