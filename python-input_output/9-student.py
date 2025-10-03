#!/usr/bin/python3
class Student:
    """Define a student with public attributes and JSON-ready dict."""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Return a dict representation of the instance (JSON-serializable)."""
        return self.__dict__
