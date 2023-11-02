#!/usr/bin/python3

import sys

def main():
    args = sys.argv[1:]
    count = len(args)
    print(f"{count} argument{'s' if count != 1 else ''}:")
    for i, arg in enumerate(args, start=1):
        print(f"{i}: {arg}")

if __name__ == "__main__":
    main()
