#!/usr/bin/python3
def square_matrix_simple(mat=[]):
    """
        mat: matrix
        smat: submatrix
        e: element
        The function takes a matrix and returns a new squared matrix
        inside the inner lambda constructor
    """
    return list(map(lambda smat: list(map(lambda e: e**2, smat)), mat))
