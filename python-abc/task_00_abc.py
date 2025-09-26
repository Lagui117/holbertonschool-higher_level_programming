#!/usr/bin/env python3
"""
Abstract Animal class and concrete subclasses Dog and Cat.

- Animal is an abstract base class with an abstract method `sound()`.
- Dog and Cat implement `sound()` and return "Bark" and "Meow" respectively.
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class representing an animal."""

    @abstractmethod
    def sound(self) -> str:
        """
        Return the sound made by the animal.

        Subclasses must override this method.
        """
        raise NotImplementedError


class Dog(Animal):
    """Concrete Animal: Dog."""

    def sound(self) -> str:
        """Return the dog's sound."""
        return "Bark"


class Cat(Animal):
    """Concrete Animal: Cat."""

    def sound(self) -> str:
        """Return the cat's sound."""
        return "Meow"
