#!/usr/bin/env python3
"""
VerboseList: extends Python's built-in list to print notifications on mutations.

- append(item):   prints "Added [item] to the list."
- extend(iter):   prints "Extended the list with [n] items."  (n = number added)
- remove(item):   prints "Removed [item] from the list." (before removing)
- pop(index=-1):  prints "Popped [item] from the list."   (before popping)
"""

from __future__ import annotations


class VerboseList(list):
    """A list that announces when items are added or removed."""

    def append(self, item) -> None:
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable) -> None:
        # Convert first to handle any iterable and to know how many items are added
        items = list(iterable)
        super().extend(items)
        print(f"Extended the list with [{len(items)}] items.")

    def remove(self, item) -> None:
        # Announce before removing (as requested)
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index: int = -1):
        # Determine the item to be popped first, then delegate to super().pop
        item = self[index]  # will raise IndexError if out of range, matching list behavior
        print(f"Popped [{item}] from the list.")
        return super().pop(index)
