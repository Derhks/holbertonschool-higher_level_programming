#!/usr/bin/python3
"""
This is the matrix_divided module and it works like this:
>>> matrix = [[1, 2, 3], [4, 5, 6]]
>>> matrix_divided(matrix, 5)
[[0.2, 0.4, 0.6], [0.8, 1.0, 1.2]]
"""


def matrix_divided(matrix, div):
    """This method divides every number of the matrix for another number


    returns a new matrix
    """

    message_1 = "matrix must be a matrix (list of lists) of integers/floats"
    message_2 = "Each row of the matrix must have the same size"
    new_matrix = [matrix_list[:] for matrix_list in matrix]

    if isinstance(matrix, list) is False:
        raise TypeError(message_1)

    elif isinstance(matrix, list) is True:
        for matrix_list in matrix:
            if isinstance(matrix_list, list) is False:
                raise TypeError(message_1)

    elif isinstance(matrix, list) is True:
        for matrix_list in matrix:
            if isinstance(matrix_list, list) is True:
                for numbers in matrix_list:
                    if isinstance(numbers, (int, float)) is False:
                        raise TypeError(message_1)

    if isinstance(matrix, list) is True:
        for matrix_list in matrix:
            if len(matrix[0]) != len(matrix[1]):
                raise TypeError(message_2)

    if isinstance(div, (int, float)) is False:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    for cnt_list in range(len(matrix)):
        for cnt_numbers in range(len(matrix[cnt_list])):
            division = round(matrix[cnt_list][cnt_numbers] / div, 2)
            new_matrix[cnt_list][cnt_numbers] = division

    return new_matrix
