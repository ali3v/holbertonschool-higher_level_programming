#!/usr/bin/python3
"""
This module contains a class
"""


class BaseGeometry:
    """
    This is an empty class
    """
    def area(self):
        """
        Function that raise exception by default
        Will be redefines in subclass for each
        geometrys
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Function that says if a value is an integer.
        Name's just there to be printed in erro message.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
