#!/usr/bin/python3
"""
    A class Rectanglethat defines a rectangle.
"""


class Rectangle:
    """
        define a rectangle with width and height.
    """
    def __init__(self, width=0, height=0):
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
