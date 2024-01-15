#!/usr/bin/python3
""" Rectangle derived class from Base """
from models.base import Base


class Rectangle(Base):
    """ Rectangle subclass implementation """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Constructor for subclass
        args:
            width (int): Width size
            height (int): Height size
            x (int, optional): X-coordinate of rectangle (0 by default)
            y (int, optional): Y-coordinate of rectangle (0 by default)
            id (int, optional): ID value default None.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ width getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter """
        self.dim_validator("width", value)
        self.__width = value

    @property
    def height(self):
        """ height getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter """
        self.dim_validator("height", value)
        self.__height = value

    @property
    def x(self):
        """ x getter method """
        return self.__x

    @x.setter
    def x(self, value):
        """ x setter method """
        self.pos_validator("x", value)
        self.__x = value

    @property
    def y(self):
        """ y getter method """
        return self.__y

    @y.setter
    def y(self, value):
        """ y setter method """
        self.pos_validator("y", value)
        self.__y = value

        ## Public Functions

    def dim_validator(self, name, value):
        """ Validate width and height """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be > 0".format(name))

    def pos_validator(self, name, value):
        """ Validate x and y """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value < 0:
            raise ValueError("{} must be >= 0".format(name))

    def area(self):
        """ Returns the area of shape """
        return self.__width * self.__height

    def display(self):
        """ Display shape using # """
        for _ in range(self.__y):
            print()
        
        for _ in range (self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """ String representation of the Rectangle instance """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args):
        """ Update attr with provided args 
        
        args:
            *args (int) : attr list
                - id
                - width
                - height
                - x
                - y

            **kwargs (dict) : keyword dictionary
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg
                a += 1
