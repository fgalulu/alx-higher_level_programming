#!/usr/bin/python3
"""Defines a rectangle with width and height."""


class Rectangle:
    """
        define a rectangle with width and height.
        Attributes:
            width(int): rectangle width.
            height(int): rectangle height.
    """
    number_of_instances = 0
    def __init__(self, width=0, height=0):
        """
            Intitialize a new Rectangle instance.
            Args:
                width(int): rectangle width.
                height(int): rectangle height.
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

        if not isinstance(height, int):
            raise TypeError("width must be an integer")
        if height < 0:
            raise ValueError("width must be >= 0")
        self.__height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """
            Get/set the width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
            Get/set the width of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Get area of the rectangle."""
        return self.__height * self.__width

    def perimeter(self):
        """Get perimeter of the rectangle."""
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """return string representation."""
        rect = ""
        if self.__height == 0 or self.__width == 0:
            return ""
        for n in range(0, self.__height):
            rect += "#" * self.__width
            if n != self.__height - 1:
                rect += '\n'
        return rect

    def __repr__(self):
        """ return string representation of rectangle.
        Should be able to create anew instance using eval()
        """
        return '{self.__class__.__name__}({self.width}, {self.height})'.\
            format(self=self)

    def __del__(self):
        """
        Prints when rectangle object is deleted.
        """
        print("Bye rectangle...")
        type(self).number_of_instances -= 1
