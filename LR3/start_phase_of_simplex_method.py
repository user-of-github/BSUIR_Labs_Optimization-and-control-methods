import copy
import pprint
import numpy as np
from basic_phase_of_simplex_method import extract_submatrix_by_column_numbers


def start_phase_of_simplex_method(matrix_a: np.array, vector_b: np.array, vector_c: np.array) -> (np.array, np.array):
    a: np.array = copy.deepcopy(matrix_a)
    b: np.array = copy.deepcopy(vector_b)
    c: np.array = copy.deepcopy(vector_c)

    rows_count: int = matrix_a.shape[0]
    columns_count: int = matrix_a.shape[1]

    # 1) remove negative rows (where b[i] < 0)

    for row_index in range(rows_count):
        if b[row_index] < 0:
            for col_index in range(columns_count):
                a[row_index][col_index] *= -1
            b[row_index] *= -1

    pprint.pprint(a)

    # 2) get auxiliary task of linear programming c_auxiliary
    c_auxiliary: np.array = np.array([0] * columns_count + [-1] * rows_count)
    identity_matrix: np.array = np.identity(rows_count)

    a_auxiliary: np.array = np.append(a, identity_matrix, axis=1)  # glue matrices horizontally

    x_auxiliary_initial_plan: np.array = np.append(np.array([0] * columns_count), b)
    b_auxiliary_initial_plan: np.array = np.array([columns_count + counter + 1 for counter in range(columns_count)])

    #a_auxiliary_base_matrix: np.array = extract_submatrix_by_column_numbers(a_auxiliary, b_auxiliary_initial_plan)
    #a_auxiliary_inverse_matrix: np.array = np.linalg.inv(a_auxiliary_base_matrix)

    print(b_auxiliary_initial_plan)
    pprint.pprint(a_auxiliary)