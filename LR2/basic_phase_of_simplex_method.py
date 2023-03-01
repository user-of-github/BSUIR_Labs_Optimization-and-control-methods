import numpy as np
import copy
import math


def basic_phase_of_simplex_method(matrix_a: np.array, vector_c: np.array, vector_x: np.array, vector_b: np.array) -> (np.array, np.array):
    a: np.array = copy.deepcopy(matrix_a)
    c: np.array = copy.deepcopy(vector_c)
    x: np.array = copy.deepcopy(vector_x)
    b: np.array = copy.deepcopy(vector_b)

    while True:
        basis_matrix: np.array = extract_submatrix_by_column_numbers(a, b)
        inverse_matrix: np.array = np.linalg.inv(basis_matrix)

        vector_cb: np.array = np.array([c[index - 1] for index in b])

        potential_vector: np.array = vector_cb.dot(inverse_matrix)  # to return np.array, not np.matrix

        grades_vector: np.array = np.subtract(potential_vector.dot(a), c)

        j0: int = get_index_of_first_negative_item(grades_vector)

        if j0 == -1:
            return x, b

        vector_z: np.array = inverse_matrix.dot(extract_submatrix_by_column_numbers(a, [j0 + 1])).flatten()

        vector_tetta = np.array([x[b[counter] - 1] / item if item > 0 else float('inf') for (counter, item) in enumerate(vector_z)])

        tetta: float | int = min(vector_tetta)

        if tetta == float('inf') or math.isinf(tetta):
            raise Exception('Function is not limited')

        replace_index: int = vector_tetta.tolist().index(tetta)

        for (index, value) in enumerate(b):
            x[value - 1] -= tetta * vector_z[index]

        b[replace_index] = j0 + 1

        x[j0] = tetta


# get matrix only of selected columns from source matrix
def extract_submatrix_by_column_numbers(source: np.array, column_numbers: list[int]) -> np.array:
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

    return np.array(response)


def get_index_of_first_negative_item(array: list) -> int:
    for counter, item in enumerate(array):
        if item < 0:
            return counter

    return -1
