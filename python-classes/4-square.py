#!/usr/bin/python3
"""Module 2-square: defines a Square with validated size."""


class Square:
    """Square class with a private size attribute."""

    def __init__(self, size=0):
        """Initialize a Square.

        Args:
            size (int): Side length of the square (default: 0).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the current square area."""
        return self.__size * self.__size

    @property
    def size(self):
        """Retrieve current size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Update size with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
