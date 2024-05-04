#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):

    rowlength = len(submatrix)
    if not matrix:
        return None
    for submatrix in matrix:
        if rowlength == 0:
            print()
        for i in range(rowlength):
            print("{:d}".format(submatrix[i]),
                  end="\n" if i is rowlength - 1 else " ")
