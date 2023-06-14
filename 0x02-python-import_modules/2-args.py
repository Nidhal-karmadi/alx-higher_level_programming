#!/usr/bin/python3

import sys

def print_arguments(argv):
    num_arguments = len(argv)
    print(f"Number of argument(s): {num_arguments}")

    if num_arguments == 0:
        print(".")
    else:
        print(":")
        for i, arg in enumerate(argv, start=1):
            print(f"{i}: {arg}")

print_arguments(sys.argv[1:])

