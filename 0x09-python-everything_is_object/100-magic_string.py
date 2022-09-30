#!/usr/bin/python3
"""returns a string “BestSchool” n times the number of the iteration"""


def magic_string():
    """returns a string “BestSchool” n times the number of the iteration"""
    setattr(magic_string, "n", getattr(magic_string, "n", 0) + 1)
    return ("Best School, " * getattr(magic_string, "n", 0))[:-2]
