#!/usr/bin/python3
"""Define a Student class with JSON-ready representation."""


class Student:
    """Student with public attributes and a dict serializer."""

    def __init__(self, first_name, last_name, age):
        """Initialize a student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Return a dict representation of the instance."""
        return self.__dict__
