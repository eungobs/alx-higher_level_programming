#!/usr/bin/python3
"""MagicClass generation module
"""


import math


class MagicClass:
    """Class defined for MagicClass generation.

    Args:
        radius (float): radius of the circle

    Attributes:
        __radius (float): radius of the circle

    """

    def __init__(self, radius=0):
        # attribute assigment here engages setter defined below
        self.radius = radius

    @property
    def radius(self):
        """__radius getter, setter with same method name

        Returns:
            __radius (float): radius of the circle

        """
        return self.__radius

    @radius.setter
    def radius(self, value):
        """Args:
            value (float): radius of the circle

        Attributes:
            __radius (float): radius of the circle

        Raises:
            TypeError: if value is not a number
            ValueError: if value is less than 0

        """
        if type(value) not in [float, int]:
            raise TypeError('radius must be a number')
        if value < 0:
            raise ValueError('radius must be >= 0')
        self.__radius = float(value)

    def area(self):
        """Calculates the area of the circle.

        Returns:
            area (float): area of the circle

        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Calculates the circumference of the circle.

        Returns:
            circumference (float): circumference of the circle

        """
        return 2 * math.pi * self.__radius
