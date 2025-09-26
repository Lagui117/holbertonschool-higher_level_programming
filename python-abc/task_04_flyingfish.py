#!/usr/bin/env python3
"""
The Enigmatic FlyingFish - Exploring Multiple Inheritance

- Fish:    swim(), habitat()
- Bird:    fly(),  habitat()
- FlyingFish(Fish, Bird): overrides fly(), swim(), habitat()
"""

from __future__ import annotations


class Fish:
    def swim(self) -> None:
        print("The fish is swimming")

    def habitat(self) -> None:
        print("The fish lives in water")


class Bird:
    def fly(self) -> None:
        print("The bird is flying")

    def habitat(self) -> None:
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    def fly(self) -> None:
        print("The flying fish is soaring!")

    def swim(self) -> None:
        print("The flying fish is swimming!")

    def habitat(self) -> None:
        print("The flying fish lives both in water and the sky!")
