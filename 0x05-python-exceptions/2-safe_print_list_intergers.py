#!/usr/bin/python3

def safe_print_list_intergers(my_list[], x=0):
    y = 0
    displayed = 0
    for y in range(0, x):
        try:
            print("{:d}".format(my_list[y]), end="")
            displayed += 1
        except (ValueError, TypeError):
            continue
        print()
        return displayed
