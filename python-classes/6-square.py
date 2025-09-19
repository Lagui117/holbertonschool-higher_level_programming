#!/usr/bin/python3
"""Module 6-square: defines a Square class with position offset."""


class Square:
    """Represents a square with a private size and position."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a Square with optional size and position."""
        self.size = size          # validation via setter
        self.position = position  # validation via setter

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size with validations."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieve the position (tuple of 2 non-negative ints)."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position with validations."""
        if (
            not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(n, int) for n in value) or
            not all(n >= 0 for n in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the current square area."""
        return self.__size * self.__size

    def my_print(self):
        """Print the square with '#', offset by position.
        If size is 0, print an empty line.
        """
        if self.__size == 0:
            print("")
            return

        # Vertical offset
        for _ in range(self.__position[1]):
            print("")

        # Each line: horizontal spaces then hashes
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
