#!/usr/bin/python3

class Square:
    """
    This class represents a square.

    Attributes:
        __size (int): The size of the square (private attribute).
    """

    def __init__(self, size):
        """
        Initializes a Square instance with the given size.

        Args:
            size (int): The size of the square.
        """
        self.__size = size

# Example usage
if __name__ == "__main__":
    square = Square(5)
    print(square.__size)  # This will not work due to name mangling, use getter methods instead

