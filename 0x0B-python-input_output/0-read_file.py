#!/usr/bin/python3
"""text file-reading function."""


def read_file(filename=""):
    """Print the contents of a UTF8 text file """
    with open(filename, encoding="utf-8") as myFile:
        print(myFile.read(), end="")
