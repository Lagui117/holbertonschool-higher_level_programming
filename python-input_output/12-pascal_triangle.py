#!/usr/bin/python3
"""Generate Pascal's triangle as a list of lists."""
 

def pascal_triangle(n):
    """Return Pascal’s triangle of size n.
    For n <= 0, return an empty list.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for _ in range(1, n):
        prev = triangle[-1]
        next_row = [1] + [prev[i] + prev[i + 1] for i in range(len(prev) - 1)] + [1]
        triangle.append(next_row)
    return triangle
