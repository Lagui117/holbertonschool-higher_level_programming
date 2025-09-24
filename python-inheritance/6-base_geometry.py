#!/usr/bin/python3
"""Base geometry module with an abstract-like area method."""


class BaseGeometry:
    """Base class for geometry operations."""

    def area(self):
        """Raise an exception because area is not implemented."""
        raise Exception("area() is not implemented")
