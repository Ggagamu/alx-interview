#!/usr/bin/python3
"""
Returns a list of integers for the Pascal’s triangle
"""


def pascal_triangle(n):
    '''
    Pascal's triangle
    Args:
      n (int): The number of rows of the triangle
    Returns:
      List of lists of integers representing the Pascal’s triangle
    '''
    if n <= 0:
        return []

    pascal_triangle = []
    for j in range(n):
        if j == 0:
            pascal_triangle.append([1])
        else:
            row = [1]
            prev_row = pascal_triangle[j-1]
            for k in range(1, j):
                row.append(prev_row[k-1] + prev_row[k])
            row.append(1)
            pascal_triangle.append(row)
    return pascal_triangle
