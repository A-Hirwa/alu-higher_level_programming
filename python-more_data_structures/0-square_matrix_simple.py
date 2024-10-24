#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    mat_list = [[x*x for x in row]for row in matrix]
    return mat_list
