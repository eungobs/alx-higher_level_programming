#!/usr/bin/python3
"""Class define for square generation
"""


class Square:
    """Class defined for square generation.

    Args:
        size (float): length of one side of square

    Attributes:
        __size (float): length of one side of square

    """

    def __init__(self, size=0):
        # attribute assigment here engages setter defined below
        self.size = size

    @property
    def size(self):
        """__size getter, setter with same method name

        Returns:
            __size (float): length of one side of square

        """
        return self.__size

    @size.setter
    def size(self, value):
        """Args:
            value (float): length of one side of square

        Attributes:
            __size (float): length of one side of square

        Raises:
            TypeError: if value is not a number
            ValueError: if value is less than 0

        """
        if type(value) not in [float, int]:
            raise TypeError('size must be a number')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = float(value)

    def area(self):
        """Calculates the area of the square.

        Returns:
            area (float): area of the square

        """
        return self.__size ** 2

    def __eq__(self, other):
        """Equality comparator method.

        Args:
            other (Square): other square to compare to

        Returns:
            bool: True if squares are equal, False otherwise

        """
        return self.area() == other.area()

    def __ne__(self, other):
        """Inequality comparator method.

        Args:
            other (Square): other square to compare to

        Returns:
            bool: True if squares are not equal, False otherwise

        """
        return self.area() != other.area()

    def __gt__(self, other):
        """Greater than comparator method.

        Args:
            other (Square): other square to compare to

        Returns:
            bool: True if self is greater than other, False otherwise

        """
        return self.area() > other.area()

    def __ge__(self, other):
        """Greater than or equal to comparator method.

        Args:
            other (Square): other square to compare to

        Returns:
            bool: True if self is greater than or equal to other, False otherwise

        """
        return self.area() >= other.area()

    def __lt__(self, other):
        """Less than comparator method.

        Args:
            other (Square): other square to compare to

        Returns:
            bool: True if self is less than other, False otherwise

        """
        return self.area() < other.area()

    def __le__(self, other):
        """Less than or equal to comparator method.

        Args:
            other (Square): other square to compare to

        Returns:
            bool: True if self is less than or equal to other, False otherwise

        """
        return self.area() <= other.area()
