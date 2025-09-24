#!/usr/bin/python3
"""Square class inheriting from Rectangle."""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square with private size, validated as a positive integer."""

    def __init__(self, size):
        """Initialize a square with validated size."""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Return the square area."""
        return self.__size * self.__size
