#!/usr/bin/python3
"""Utility to introspect objects (list attributes and methods)."""


def lookup(obj):
    """Return the list of available attributes and methods of `obj`."""
    return dir(obj)
