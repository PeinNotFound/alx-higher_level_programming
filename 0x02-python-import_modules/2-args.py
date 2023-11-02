#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    numbers = len(sys.argv) - 1

    if numbers == 0:
        print("{} arguments.".format(numbers))
    elif numbers == 1:
        print("{} argument:".format(numbers))
    else:
        print("{} arguments:".format(numbers))

    if numbers >= 1:
        numbers = 0
        for arg in sys.argv:
            if numbers != 0:
                print("{}: {}".format(numbers, arg))
            numbers += 1
