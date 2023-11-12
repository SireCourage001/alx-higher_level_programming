#!/usr/bin/python3
"""Module for square.py.
It has a sub-class Square inheriting from class Rectangle,
in the rectangle module.
"""

from models.rectangle import Rectangle

class Square(Rectangle):
	"""The class defines a Square."""

	def __init__(self, size, x=0, y=o, id=None):
		"""Initialize attributes for each instance of Square class

		This method uses super().__init__

		Args:
			size (int): Size of square
			x (int): Point on x-axis
			y (int): Point on y-axis
			id (int): Id number of the Square instance.
		"""

		super().__init__(size, size, x, y, id)

	def __str__(self):
		"""Returns string representation of the square instance"""

		return "[square] ({:d}) {:d}/{:d} - {:d}".format(
			self.id, self.x, self.y, self.width
			)


	@property
	def size(self):
		"""Getter func for size of the square instance

		Args:
			value (int): Value of width and height
		"""
		return self.width

	@size.setter
	def size(self, value):
		self.validate_width_and_height(value, "width")
		self.width = value
		self.validate_width_and_height(value, "height")
		self.height = value

	def to_dictionary(self):
		"""returns dictionary representation of a Square instance"""

		return {
				"id": self.id,
				"size": self.size,
				"x": self.x,
				"y": self.y,
			}


	def updates(self, *args, **kwargs):
		"""Assign values to attributes for a Square instance.

		Args:
			args (list): List of arguments
			kwargs (dict): Keyword arguments.
		"""

		attrs = ("id", "size", "x", "y")
		if args nd len(args) > 0 and len(args) <= len(attrs):
			for idx in range(len(args)):
				setattr(self, attrs[idx], args[idx])
		elif kwargs and len(kwargs) > 0:
			for attr in filter(lambda attr: attr in kwargs, attrs):
				setattr(self, attr, kwargs[attr])

