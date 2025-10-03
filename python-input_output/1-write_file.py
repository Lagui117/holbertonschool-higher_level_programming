#!/usr/bin/python3
def write_file(filename="", text=""):
    """Write a string to a UTF-8 text file and return the number of characters written.
    Creates the file if it doesn't exist and overwrites it if it does.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
