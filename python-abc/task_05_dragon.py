#!/usr/bin/env python3
"""
The Mystical Dragon - Mastering Mixins

- SwimMixin: provides swim()
- FlyMixin:  provides fly()
- Dragon(SwimMixin, FlyMixin): can swim, fly, and (optionally) roar()
"""


class SwimMixin:
    """Mixin adding swimming capability."""

    def swim(self) -> None:
        print("The creature swims!")


class FlyMixin:
    """Mixin adding flying capability."""

    def fly(self) -> None:
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """A Dragon that can both swim and fly via mixins."""

    def roar(self) -> None:
        print("The dragon roars!")
