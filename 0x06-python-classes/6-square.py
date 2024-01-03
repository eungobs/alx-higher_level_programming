#!/usr/bin/python3
"""Square generation module
"""


class Square:
    """Class defined for square generation.

    Args:
        size (int): length of one side of square
        position (tuple): position of the square in 2D space

    Attributes:
        __size (int): length of one side of square
        __position (tuple): position of the square in 2D space

    """

    def __init__(self, size=0, position=(0, 0)):
        # attribute assigment here engages setters defined below
        self.size = size
        self.position = position

    @property
    def size(self):
        """__size getter, setter with same method name

        Returns:
            __size (int): length of one side

        """
        return self.__size

    @size.setter
    def size(self, value):
        """Args:
            value (int): length of one side

        Attributes:
            __size (int): length of one side

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than 0

        """
        if type(value) is not int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        """__position getter, setter with same method name

        Returns:
            __position (tuple): position of square in 2D space

        """
        return self.__position

    @position.setter
    def position(self, value):
        """Args:
            value (tuple): position of square in 2D space

        Attributes:
            __position (tuple): position of square in 2D space

        Raises:
            TypeError: if value is not a tuple of 2 positive integers

        """
        if type(value) is not tuple or len(value) != 2 \
                or type(value[0]) is not int or type(value[1]) is not int \
                or value[0] < 0 or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """Calulates area of square.

        Attributes:
            __size (int): length of one side of square

        Returns:
            area (int): length of one side, squared

        """
        area = self.__size * self.__size
        return area

    def my_print(self):
        """Prints text representation of square in hash chars.

        Attributes:
            __size (int): length of one side of square
            __position (tuple): position of square in 2D space

        """
        if self.__size == 0:
            print()
            return
        for row in range(0, self.__position[1]):
            print()
        for row in range(0, self.__size):
            for col in range(0, self.__position[0]):
                print(" ", end="")
            for col in range(0, self.__size):
                print("#", end="")
            print()
