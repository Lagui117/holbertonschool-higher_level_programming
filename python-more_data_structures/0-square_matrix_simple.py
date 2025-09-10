#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in matrix:
        row = []
        for j in range(len(i)):
            row.append(i[j] ** 2)
        new_matrix.append(row)
    return new_matrix
