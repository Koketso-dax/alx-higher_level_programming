#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    copy = [[0] * len(matrix[0]) for _ in range(len(matrix))]
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            copy[x][y] = matrix[x][y] ** 2
    return copy
