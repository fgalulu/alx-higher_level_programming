#!/usr/bin/python3
"""
This is the 0-add_integer module.

It suplies one function, add_integer(a, b)
"""
def add_integer(a, b=98):
    """My addition function
        Args:
            a: first integer
            b: second integer which have a default value 98
        Returns:
            The return value. a + b
    """

    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b
