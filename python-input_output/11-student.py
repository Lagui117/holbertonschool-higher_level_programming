#!/usr/bin/python3
class Student:
    """Define a student with JSON (de)serialization helpers."""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return a dict representation of the instance.

        If attrs is a list of strings, only those attributes (if present) are included.
        Otherwise, return all public attributes.
        """
        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of the instance from a dict."""
        for k, v in json.items():
            setattr(self, k, v)
