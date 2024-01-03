#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """
    Computes the square value of all integers of a matrix
    ...

    Parameters
    ----------
    matrix : list (of lists)
        The list of elements

    Return:
        a new matrix:
         Same size as matrix
         Each value should be the square of the value of the input
    """

<<<<<<< HEAD
    return [[x * x for x in row] for row in matrix]

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

squared_matrix = square_matrix_simple(matrix)

for orig_row, squared_row in zip(matrix, squared_matrix):
    print(orig_row, squared_row)
=======
    return ([list(map(lambda x: x * x, row)) for row in matrix])
>>>>>>> a0a689791b04a7744b3c1ade2c7b18275f82b799
