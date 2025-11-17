#!/usr/bin/python3
"""
This module defines a Square class representing a square with a private size attribute.
"""

class Square:
    """Represent a square with a private size attribute."""

    def __init__(self, size):
        """
        Initialize a new Square.

        Args:
            size (int): The size of the square.
        """
        self.__size = size
