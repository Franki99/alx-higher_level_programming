#!/usr/bin/python3

"""Define a MagicClass"""

import math


class MagicClass:
    """Circle representation"""

    def __init__(self, radius=0):
        """Initialize a MagicClass

        Arg:
            radius (float or int): The radius of the new MagicClass
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            if type(radius) is not int and type(radius) is not float:
        self.__radius = radius
    def area(self):
        """Returns the area of the MagicClass."""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """Returns The circumference of the MagicClass."""
        return (2 * math.pi * self.__radius)
