#!/usr/bin/python3
"""Module 1-rectangle: defines a Rectangle with validated width/height."""


class Rectangle:
    """Defines a rectangle with private width and height."""

    def __init__(self, width=0, height=0):
        """Initialize a Rectangle with optional width and height."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieve the width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width with validations."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the height."""
        return self.__
