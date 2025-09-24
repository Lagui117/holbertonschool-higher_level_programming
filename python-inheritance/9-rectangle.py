#!/usr/bin/python3
"""Rectangle class inheriting from BaseGeometry with area and str()."""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle with private width and height, validated as integers."""

    def __init__(self, width, height):
        """Initialize rectangle after validating width and height."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Return the rectangle area."""
        return self.__width * self.__height

    def __str__(self):
        """Return printable description: [Rectangle] <width>/<height>."""
        return f"[Rectangle] {self.__width}/{self.__height}"

