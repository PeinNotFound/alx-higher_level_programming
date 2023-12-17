#!/usr/bin/python3
"""This is a definition of a class named Square."""

class Square:
    """This class represents square."""

    def __init__(self, size=0):
        """
        Constructor for Square class.

        Args:
            size (int): size of the square's sides.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
