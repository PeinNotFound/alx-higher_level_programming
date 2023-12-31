#!/usr/bin/python3
''' defining int and adding fun'''
def add_integer(a, b=98):
    '''Return the integer addition of a&b'''
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
