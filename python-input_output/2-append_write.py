#!/usr/bin/python3
"""Append text to a UTF-8 file and return the number of chars added."""


def append_write(filename="", text=""):
    """Append `text` at the end of `filename` (UTF-8).

    Creates the file if it doesn't exist and returns the number
    of characters added.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
