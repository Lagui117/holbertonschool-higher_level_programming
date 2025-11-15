#!/usr/bin/python3
"""
Module that prints a text with 2 new lines after . ? and :

This module contains one function: text_indentation(text)
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: . ? :

    Args:
        text: A string to print with indentation

    Raises:
        TypeError: If text is not a string

    Example:
        >>> text_indentation("Hello. How are you?")
        Hello.
        <BLANKLINE>
        How are you?
        <BLANKLINE>
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Skip leading spaces
    start = 0
    while start < len(text) and text[start] == ' ':
        start += 1

    # If only spaces, return without printing
    if start >= len(text):
        return

    i = start
    while i < len(text):
        print(text[i], end="")

        if text[i] in ".?:":
            print("\n")
            # Skip spaces after the delimiter
            i += 1
            while i < len(text) and text[i] == ' ':
                i += 1
            continue

        i += 1
