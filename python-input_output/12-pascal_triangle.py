#!/usr/bin/python3
def pascal_triangle(n):
    """Return the Pascal’s triangle of n as a list of lists.
    If n <= 0, return an empty list.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for _ in range(1, n):
        prev = triangle[-1]
        # Construire la ligne suivante : 1, (somme des voisins), 1
        next_row = [1] + [prev[i] + prev[i + 1] for i in range(len(prev) - 1)] + [1]
        triangle.append(next_row)
    return triangle
