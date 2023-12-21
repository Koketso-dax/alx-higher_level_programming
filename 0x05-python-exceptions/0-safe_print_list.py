#!/usr/bin/python3


safe_print_list(my_list=[], x=0):
    y = 0
    displayed = 0
    for y in range(0, x):
        try:
            print("{}".format(my_list[y]), end="")
            displayed += 1
        except:
            continue
    print()
    return displayed
