#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda row: list(map(lambda cnt2: cnt2 ** 2, row)), matrix))
