#!/usr/bin/python3
"""Read a UTF-8 text file and print its content to stdout."""
def read_file(filename=""):
    """Read a file (UTF-8) and print its content to stdout, unchanged."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
