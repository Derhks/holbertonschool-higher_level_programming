#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = [cnt[:] for cnt in matrix]
    for cnt1 in range(len(new_matrix)):
        for cnt2 in range(len(new_matrix[cnt1])):
            new_matrix[cnt1][cnt2] = matrix[cnt1][cnt2] ** 2
    return new_matrix
