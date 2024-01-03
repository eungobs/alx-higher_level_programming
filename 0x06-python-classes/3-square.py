#!/usr/bin/python3
"""Class square generation
"""


class Square:
    """Class defined for square generation.

    Attributes:
        __size (int): length of one side of square

    """

    def __init__(self, size=0):
        """Args:
            size (int): length of one side of square

        Attributes:
            __size (int): length of one side of square

        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0

        """
        if type(size) != int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """Calculates the area of the square.

        Returns:
            int: area of the square

        """
        return self.__size ** 2
