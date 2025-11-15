#!/usr/bin/python3
"""
This module provides a function that divides all elements of a matrix
by a given number, with specific error handling
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number.

    Args:
        matrix (list): A list of lists containing integers or floats.
        div (int or float): The number to divide each matrix element by.

    Returns:
        list: A new matrix with all elements divided
        by div and rounded to 2 decimal places

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats,
                   if each row of the matrix doesn't have the same size,
                   or if div is not a number.
        ZeroDivisionError: If div is equal to 0.
    """
    errorMessage = (
        "matrix must be a matrix (list of lists) "
        "of integers/floats"
    )

    if not matrix or not isinstance(matrix, list):
        raise TypeError(errorMessage)

    if matrix == [] or matrix == [[]]:
        raise TypeError(errorMessage)

    if not matrix or matrix == [[]]:
        raise TypeError(errorMessage)

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(errorMessage)

        for item in row:
            if not isinstance(item, (int, float)):
                raise TypeError(errorMessage)

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(item / div, 2) for item in row] for row in matrix]
