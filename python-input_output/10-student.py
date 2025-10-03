#!/usr/bin/python3
"""Define a Student class with filtered JSON representation."""


class Student:
    """Student with public attributes and a filtered dict serializer."""

    def __init__(self, first_name, last_name, age):
        """Initialize a student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return a dict representation of the instance.

        If attrs is a list of strings, return only those attributes present.
        Otherwise, return all public attributes.
        """
        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
