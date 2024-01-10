#!/usr/bin/python3

"""
    Contains the lookup function code
"""
def lookup(obj):
    """Lookup returns all availale objects in an objects dictionary as a list:
    Args:
        obj: Python object
    Returns:
        list: List of attributes
    """
    return dir(obj)
