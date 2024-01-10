#!/usr/bin/python3


def lookup(obj):
    """
    returns all availale objects in an objects dictionary
    as a list

    :param obj: Python object
    :return: List of attributes
    """
    return dir(obj)
