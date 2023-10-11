#!/usr/bin/python3
"""Pascal's Triangle function."""


def pascal_triangle(n):
    """Represent Pascal's Triangle of size n."""
    if n <= 0:
        return []

    tr = [[1]]
    while len(tr) != n:
        tri = tr[-1]
        tmp = [1]
        for i in range(len(tri) - 1):
            tmp.append(tri[i] + tri[i + 1])
        tmp.append(1)
        tr.append(tmp)
    return tr
