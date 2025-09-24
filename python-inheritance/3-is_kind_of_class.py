#!/usr/bin/python3
"""Module that defines a function to check if an object
is an instance of a class or a class that inherited from it.
"""


def is_kind_of_class(obj, a_class):

    """Return True if obj is an instance of a_class
    or a class inherited from a_class, otherwise False.
    """
    return isinstance(obj, a_class)
