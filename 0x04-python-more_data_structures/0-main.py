#!/usr/bin/env python3

square_matrix_simple = __import__('0-square_matrix_simple').square_matrix_simple

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

result = square_matrix_simple(matrix)
for row in result:
    print(row)
