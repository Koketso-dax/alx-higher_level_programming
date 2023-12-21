#!/usr/bin/python3


def safe_print_division(a, b):
    """
    returns the quotient of two numbers @a and @b
    and prints the result whilst handling divide by zero exception
    """
    try:
        c = a / b
    except:
        c = None
    finally:
        print("Inside result: {}".format(c))
    return c
