#!/usr/bin/python3
"""Custom list subclass with a method to print a sorted view."""

class MyList(list):
    """List subclass that can print itself sorted without modifying content."""

    def print_sorted(self):
        """Print the list items in ascending order without in-place changes."""
        print(sorted(self))
