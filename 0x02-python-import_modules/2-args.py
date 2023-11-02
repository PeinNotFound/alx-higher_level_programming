#!/usr/bin/python3

import sys

def print_arguments():
    num_args = len(sys.argv) - 1

    if num_args == 0:
        print("No arguments.")
    elif num_args == 1:
        print("1 argument:")
    else:
        print(f"{num_args} arguments:")

    for index, arg in enumerate(sys.argv[1:], 1):
        print(f"{index}: {arg}")

if __name__ == "__main__":
    print_arguments()
