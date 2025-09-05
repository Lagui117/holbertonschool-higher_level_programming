#!/usr/bin/python3
import sys

if __name__ == "__main__":
    number_of_arguments = len(sys.argv) - 1

    if number_of_arguments == 0:
        print("0 arguments.")
    elif number_of_arguments == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(number_of_arguments))

    i = 1
    while i <= number_of_arguments:
        print("{:d}: {}".format(i, sys.argv[i]))
        i += 1
