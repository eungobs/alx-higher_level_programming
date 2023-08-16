#!usr/bin/bash/python3
def square_matrix_simple(matrix=[]):
    # Create an empty matrix to store squared values
    squared_matrix = []
    
    # Iterate through each row in the input matrix
    for row in matrix:
        squared_row = []
        
        # Iterate through each element in the row and square it
        for element in row:
            squared_element = element ** 2
            squared_row.append(squared_element)
        
        # Add the squared row to the squared matrix
        squared_matrix.append(squared_row)
    
    return squared_matrix

# Example matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Call the function and print the result
result = square_matrix_simple(matrix)
for row in result:
    print(row)
