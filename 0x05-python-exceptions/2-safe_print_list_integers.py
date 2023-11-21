#!/usr/bin/python3
def safe_print_list_integers(my_list=None, x=0):
    if my_list is None
        my_list = []
    res = 0
    for a in range(0, x):
        try:
            print("{:d}".format(my_list[a]), end="")
            res += 1
        except (ValueError, TypeError):
            continue
    print("")
    return res
