#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_a_dictionary = {}
    for i, j in a_dictionary.items():
        new_a_dictionary[i] = j * 2
    return new_a_dictionary
