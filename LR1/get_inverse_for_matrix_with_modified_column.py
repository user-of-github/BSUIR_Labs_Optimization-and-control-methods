import copy
import pprint
import typing
import numpy as np


def read_square_matrix_from_file(file_name: str) -> (int, np.matrix):
    file: typing.IO = open(file_name, 'r')
    lines: list[str | bytes] = file.readlines()
    file.close()

    raw_matrix: list[list[int]] = list()
    matrix_size: int = int(lines[0])

    for rows_counter in range(1, matrix_size + 1):
        raw_matrix.append([int(x) for x in lines[rows_counter].split(' ')])

    return matrix_size, np.matrix(raw_matrix)


def read_column_from_file(file_name: str) -> (int, np.array):
    file: typing.IO = open(file_name, 'r')
    lines: list[str | bytes] = file.readlines()
    file.close()

    return int(lines[0]), np.array([int(item) for item in lines[1].split(' ')])


def get_inverse_for_matrix_with_modified_column(matrix_file_name: str, column_file_name: str) -> np.matrix | None:
    matrix_dimension, matrix = read_square_matrix_from_file(matrix_file_name)

    print('Source matrix:')
    pprint.pprint(matrix)

    print('\nReverse matrix:')
    reversal_matrix: np.matrix = np.linalg.inv(matrix)
    pprint.pprint(reversal_matrix)

    column_number, replacing_column = read_column_from_file(column_file_name)
    replacing_column = replacing_column.reshape(-1,1)

    print(f'\nThis column will replace #{column_number}:')
    pprint.pprint(replacing_column)

    l = reversal_matrix * replacing_column

    print('\nl vector equals: ')
    pprint.pprint(l)

    if l[column_number - 1][0] == 0:
        return None

    l_with_roof = copy.deepcopy(l)
    l_with_roof[column_number - 1] = -1

    l_with_triangle = l_with_roof * (-1 / l[column_number - 1])

    Q = np.identity(len(matrix))

    for row in range(0, len(Q)):
        Q[row][column_number - 1] = l_with_triangle[row]

    response = Q * reversal_matrix

    return response
