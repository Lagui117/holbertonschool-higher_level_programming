#!/usr/bin/env python3
"""
Shapes, Interfaces, and Duck Typing

- Shape: abstract base class with abstract methods `area()` and `perimeter()`.
- Circle and Rectangle: concrete implementations.
- shape_info(obj): relies on duck typing (no isinstance), prints area/perimeter.
"""

from __future__ import annotations
from abc import ABC, abstractmethod
from math import pi
from typing import Any


class Shape(ABC):
    """Abstract blueprint for 2D shapes."""

    @abstractmethod
    def area(self) -> float:
        """Return the area of the shape."""
        raise NotImplementedError

    @abstractmethod
    def perimeter(self) -> float:
        """Return the perimeter (circumference) of the shape."""
        raise NotImplementedError


class Circle(Shape):
    """Circle defined by its radius."""

    def __init__(self, radius: float) -> None:
        self.radius = float(radius)

    def area(self) -> float:
        return pi * (self.radius ** 2)

    def perimeter(self) -> float:
        return 2 * pi * self.radius


class Rectangle(Shape):
    """Rectangle defined by width and height."""

    def __init__(self, width: float, height: float) -> None:
        self.width = float(width)
        self.height = float(height)

    def area(self) -> float:
        return self.width * self.height

    def perimeter(self) -> float:
        return 2 * (self.width + self.height)


def shape_info(obj: Any) -> None:
    """
    Print area and perimeter of an object that *behaves like* a Shape.
    Duck typing: no isinstance checks—assumes `obj.area()` and `obj.perimeter()`.
    """
    print(f"Area: {obj.area()}")
    print(f"Perimeter: {obj.perimeter()}")
