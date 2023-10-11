#!/usr/bin/python3
"""file-append-writing function."""


def append_write(filename="", text=""):
    """Appends a string to the end of a UTF8 text file."""
    with open(filename, "a", encoding="utf-8") as myFile:
        return myFile.write(text)
