#!/usr/bin/python3
"""
    A class Rectangle that defines a rectangle with width and height.
"""


class Rectangle:
    """
        define a rectangle with width and height.

        Attributes:
            width(int): rectangle width.
            height(int): rectangle height.
    """
    def __init__(self, width=0, height=0):
        """
            Intitialize a new Rectangle instance.

            Args:
                width(int): rectangle width.
                height(int): rectangle height.
        """
        self.width = width
        self.height = height

    def width(self, value*):
        if value:
            self.width = value
        else:
            return self.width

    def height(self, value*):
        if value:
            self.height = value
        else:
            return self.height
