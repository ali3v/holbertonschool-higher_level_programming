#!/usr/bin/python3
"""BaseGeometry class with area() and integer_validator() methods."""


class BaseGeometry:
    """BaseGeometry class."""

    def area(self):
        """Public instance method that raises an exception."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that value is an integer greater than 0."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
