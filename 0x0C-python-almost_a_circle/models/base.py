#!/usr/bin/python3
""" Base Class Module """


class Base:
    """ Base(super) class definition """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Base Class Constructor
        args:
            id(int, optional): identifier for class instance
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
