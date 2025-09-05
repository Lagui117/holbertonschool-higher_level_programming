#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    total_of_arguments = 0
    i = 1
    while i < len(sys.argv):
        total_of_arguments += int(sys.argv[i])
        i += 1
    print("{}".format(total_of_arguments))

