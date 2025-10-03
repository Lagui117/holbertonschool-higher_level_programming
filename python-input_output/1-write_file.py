#!/usr/bin/python3
"""Write text to a file (UTF-8) and return number of characters written."""
def write_file(filename="", text=""):
    """Write `text` to `filename`, overwriting/creating it, and return count."""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
