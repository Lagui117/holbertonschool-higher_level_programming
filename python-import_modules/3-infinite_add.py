#!/usr/bin/python3
import sys
number_of_arguments = len(sys.argv)
total_of_arguments = 0

i = 1
while i < len(sys.argv):
    int(sys.argv[i])
    total_of_arguments += int(sys.argv[i])
    i += 1
print("{}".format(total_of_arguments))
