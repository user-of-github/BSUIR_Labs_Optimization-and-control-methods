import copy
import pprint

import numpy as np


def basic_phase_of_simplex_method(matrix_a: np.array, vector_c: np.array, vector_x: np.array, vector_b: np.array) -> (np.array, np.array):
    a: np.array = copy.deepcopy(matrix_a)
    c: np.array = copy.deepcopy(vector_c)
    x: np.array = copy.deepcopy(vector_x)
    b: np.array = copy.deepcopy(vector_b)

    iterations_count: int = 0

    basis_matrix: np.array = extract_submatrix_by_column_numbers(a, b)
    inverse_matrix: np.array = np.linalg.inv(basis_matrix)

    vector_cb: np.array = np.array([c[index - 1] for index in b])

    potential_vector: np.array = inverse_matrix.dot(vector_cb)

    grades_vector: np.array = np.subtract(potential_vector.dot(a), c)


# get matrix only of selected columns from source matrix
def extract_submatrix_by_column_numbers(source: np.array, column_numbers: list[int]) -> np.matrix:
    # create empty matrix
    response_columns_count: int = len(column_numbers)
    response_rows_count: int = len(source)

    response: list[list[int]] = [[0] * response_columns_count for _ in range(response_rows_count)]

    # fill it
    current_filled_column: int = 0
    for col_number in column_numbers:
        for row_number in range(response_rows_count):
            response[row_number][current_filled_column] = source[row_number][col_number - 1]

        current_filled_column += 1

    return np.matrix(response)
