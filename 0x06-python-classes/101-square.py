#!/usr/bin/python3
"""Class define for square
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
        """Calculate area of square.

        Returns:
            area (int): area of square

        """
        return self.__size ** 2

    def my_print(self):
        """Prints square using '#' character.

        """
        if self.__size == 0:
            print()
            return
        for i in range(self.__position[1]):
            print()
        for i in range(self.__size):
            for j in range(self.__position[0]):
                print(' ', end='')
            for j in range(self.__size):
                print('#', end='')
            print()

    def __str__(self):
        """String representation of Square instance.

        Returns:
            str: string representation of Square instance

        """
        s = ''
        if self.__size == 0:
            s += '\n'
            return s
        for i in range(self.__position[1]):
            s += '\n'
        for i in range(self.__size):
            for j in range(self.__position[0]):
                s += ' '
            for j in range(self.__size):
                s += '#'
            s += '\n'
        return s.strip()
