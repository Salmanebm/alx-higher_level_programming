#!/usr/bin/python3
"""class Student."""


class Student:
    """Represent a student."""

    def __init__(self, first_name, last_name, age):
        """Initial a new Student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """dictionary representation of the Student."""
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
