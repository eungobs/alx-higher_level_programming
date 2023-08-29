#!/usr/bin/python3
"""Defines a class Square."""

class Square:
    """This class represents a square."""

    def __init__(self, size):
        """Initializes a Square instance with the given size.

        Args:
            size (int): The size of the square.
        """
        self.__size = size

if __name__ == "__main__":
    square = Square(5)
    print(square._Square__size)
