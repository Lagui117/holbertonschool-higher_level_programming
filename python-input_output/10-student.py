#!/usr/bin/python3
class Student:
    """Define a student with public attributes and a filtered JSON dict."""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return a dict representation of the instance.

        If attrs is a list of strings, only those attribute names are included
        (and only if they exist on the instance). Otherwise, return all attrs.
        """
        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
