#!/usr/bin/python3
"""Define inherited list class MyList."""


class MyList(list):
    """Implements sorted printing for the list class."""

    def print_sorted(self):
        """Print a list in sorted order."""
        print(sorted(self))
