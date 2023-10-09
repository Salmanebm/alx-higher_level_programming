#!/usr/bin/python3
"""Defines an object attribute lookup."""


def lookup(obj):
    """Return a list of object's avail attribute."""
    return (dir(obj))
