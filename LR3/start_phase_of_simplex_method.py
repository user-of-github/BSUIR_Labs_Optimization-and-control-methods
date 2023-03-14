import copy
import numpy as np
from basic_phase_of_simplex_method import basic_phase_of_simplex_method
from basic_phase_of_simplex_method import extract_submatrix_by_column_numbers


def start_phase_of_simplex_method(matrix_a: np.array, vector_b: np.array) -> (np.array, np.array, np.array, np.array):
    a: np.array = copy.deepcopy(matrix_a)
    b: np.array = copy.deepcopy(vector_b)

    rows_count: int = matrix_a.shape[0]
    columns_count: int = matrix_a.shape[1]

    # 1) remove negative rows (where b[i] < 0)
    for row_index in range(rows_count):
        if b[row_index] < 0:
            for col_index in range(columns_count):
                a[row_index][col_index] *= -1
            b[row_index] *= -1

    # 2) get auxiliary task of linear programming c_auxiliary
    c_auxiliary: np.array = np.array([0] * columns_count + [-1] * rows_count)
    identity_matrix: np.array = np.identity(rows_count)

    a_auxiliary: np.array = np.append(a, identity_matrix, axis=1)  # glue matrices horizontally

    # 3)
    x_auxiliary_initial_plan: np.array = np.append(np.array([0] * columns_count), b)
    b_auxiliary_initial_plan: np.array = np.array([columns_count + counter + 1 for counter in range(rows_count)])

    # 4) solve auxiliary task by main(basic) phase of simplex method
    auxiliary_response = basic_phase_of_simplex_method(a_auxiliary, c_auxiliary, x_auxiliary_initial_plan, b_auxiliary_initial_plan)
    x_basis_plan, b_basis_indexes = auxiliary_response

    # 5) check the conditions of jointness // условия совместности
    for index in range(columns_count, a_auxiliary.shape[0]):
        if x_basis_plan[index] != 0:
            raise Exception('The task is not joint and the method completes its work')

    while max(b_basis_indexes) > columns_count + 1:
        # 6)
        j_k: int = np.max(b_basis_indexes)
        k: int = b_basis_indexes.tolist().index(j_k) + 1
        i: int = j_k - columns_count

        j_vector: list = [i for i in range(1, columns_count + 1) if i <= columns_count + 1 and i not in b_basis_indexes.tolist()]

        a_base_matrix: np.array = extract_submatrix_by_column_numbers(a_auxiliary, b_basis_indexes.tolist())
        inverse_matrix: np.array = np.linalg.inv(a_base_matrix)

        for j in j_vector:
            # print('Inverse \n', inverse_matrix)
            # print('submatrix \n', extract_submatrix_by_column_numbers(a_auxiliary, [j]))
            l_j = np.matmul(inverse_matrix, extract_submatrix_by_column_numbers(a_auxiliary, [j]))
            # print(l_j)

            if l_j[k - 1] != 0:
                b_basis_indexes[k - 1] = j - 1
            else:
                a_auxiliary = np.array(a_auxiliary[:j-1])
                a = np.array(a[:j-1])

                b_basis_indexes = np.delete(b_basis_indexes, np.argwhere(b_basis_indexes == j_k))  # remove by value
                b = np.delete(b, np.argwhere(b == b[j-1]))

                break

    return x_basis_plan[:columns_count], b_basis_indexes, a, b
