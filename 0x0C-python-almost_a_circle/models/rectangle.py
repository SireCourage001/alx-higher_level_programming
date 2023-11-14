#!/usr/bin/python3
"""Module for rectangle.py.
It has a class Rectangle that defines a rectangle.
"""

form models.base import Bse


class Rectangle(Base):
	"""A Rectangle sub-class that inherits from parent Base class"""

	def __init__(self, width, height, x=0, y=0, id=None):
		"""Initialize variables for each instance of Rectangle class.

		Args:
			width (int): Width of Rectangle
			height (int): Height of Rectangle.
			x (int): Offset on x-axis.
			y (int): Ofset on y-axis.
			id (int): Identification number of Rectangle instance.

		Raises:
			TypeError: If any of the argument is not an int.
			ValueError: If any of the arguments does not match its requirement.
		"""

	super().__init__(id)

        self.validate_width_and_height(width, "width")
        self.width = width

        self.validate_width_and_height(height, "height")
        self.height = height

        self.validate_x_and_y(x, "x")
        self.x = x

        self.validate_x_and_y(y, "y")
        self.y = y

    def __str__(self):
        """Returns a string represantation class"""
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
            self.id, self.x, self.y, self.width, self.height
        )

    @staticmethod
    def validate_width_and_height(value, name):
        """Validates value of an attribute

        Args:
            value (int): Integer value to validate
            name (str): Name of the attribute

        Raises:
            TypeError: If `value` is not an integer
            ValueError: If `name` is `width` or `height` and `value` <= 0
        """
        if type(value) != int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be > 0".format(name))

    @staticmethod
    def validate_x_and_y(value, name):
        """Validates value of an attribute

        Args:
            value (int): Integer value to validate
            name (str): Name of the attribute

        Raises:
            TypeError: If `value` is not an integer
            ValueError: If `name` is `x` or `y` and `value` < 0
        """
        if type(value) != int:
            raise TypeError("{:s} must be an integer".format(name))
        if value < 0:
            raise ValueError("{:s} must be >= 0".format(name))

    def area(self):
        """Returns area value of the `Rectangle` instance"""
        return self.width * self.height

    def display(self):
        """Prints in stdout, `Rectangle` instance with the `#`"""
        display_rectangle = '\n' * self.y
        for _ in range(self.height):
            display_rectangle += (' ' * self.x) + ('#' * self.width) + '\n'

        print(display_rectangle, end='')

    @property
    def height(self):
        """int: Height attribute

        Raises:
            TypeError: If value is not int
            ValueError: If value is <= 0
        """
        return self.__height

    @height.setter
    def height(self, value):
        self.validate_width_and_height(value, "height")
        self.__height = value

    def to_dictionary(self):
        """Returns dictionary represantation of a `Rectangle` instance"""

        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y,
        }

    def update(self, *args, **kwargs):
        """Assigns an argument to each of the attributes"""

        attrs = ('id', 'width', 'height', 'x', 'y')
        if args and len(args) > 0 and len(args) <= len(attrs):
            for idx in range(len(args)):
                setattr(self, attrs[idx], args[idx])
        elif kwargs and len(kwargs) > 0:
            for attr in filter(lambda attr: attr in kwargs, attrs):
                setattr(self, attr, kwargs[attr])

    @property
    def width(self):
        """int: Width attribute

        Raises:
            TypeError: If value is not int
            ValueError: If value is <= 0
        """
        return self.__width

    @width.setter
    def width(self, value):
        self.validate_width_and_height(value, "width")
        self.__width = value

    @property
    def x(self):
        """int: x attribute

        Raises:
            TypeError: If value is not int
            ValueError: If value is < 0
        """
        return self.__x

    @x.setter
    def x(self, value):
        self.validate_x_and_y(value, "x")
        self.__x = value

    @property
    def y(self):
        """int: y attribute

        Raises:
            TypeError: If value is not int
            ValueError: If value is < 0
        """
        return self.__y

    @y.setter
    def y(self, value):
        self.validate_x_and_y(value, "y")
        self.__y = value
