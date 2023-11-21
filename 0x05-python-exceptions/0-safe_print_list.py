#!/usr/bin/python3

def safe_print_list(my_list=None, x=0):
    if my_list is None:
        my_list = []

    a = 0
    for a in range(x):
        try:
            print("{}".format(my_list[a]), end="")
        except IndexError:
            break
        else:
            a += 1
    print("")
    return a
