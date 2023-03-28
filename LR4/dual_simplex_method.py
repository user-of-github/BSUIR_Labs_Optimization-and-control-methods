import numpy as np
import copy
from utils import extract_submatrix_by_column_numbers


def dual_simplex_method(a_matrix: np.array, b_vector: np.array, b_base_indices_vector: np.array, c_vector: np.array) -> np.array:
    a: np.array = copy.deepcopy(a_matrix)
    b: np.array = copy.deepcopy(b_vector)
    b_basis_indices: np.array = copy.deepcopy(b_base_indices_vector)
    c: np.array = copy.deepcopy(c_vector)

    while True:
        # STEP 1
        a_basis_matrix: np.array = extract_submatrix_by_column_numbers(a, b_basis_indices.tolist())
        a_basis_matrix_inverse: np.array = np.linalg.inv(a_basis_matrix)

        # STEP 2
        c_basis: np.array = np.array([c[index - 1] for index in b_basis_indices])

        # STEP 3
        y: np.array = np.matmul(c_basis, a_basis_matrix_inverse)

        # STEP 4
        k_b: np.array = np.matmul(a_basis_matrix_inverse, b)
        k: np.array = get_pseudoplan(c, b_basis_indices, k_b)

        # STEPS 5 - 6
        j_k: int = -1

        for index in range(len(k) - 1, -1, -1):
            if k[index] < 0:
                j_k = index + 1
                break

        # all are >= 0
        if j_k == -1:
            return k

        j_k_index: int = b_basis_indices.tolist().index(j_k) + 1

        # STEP 7
        delta_y_vector: np.array = np.array(a_basis_matrix_inverse[j_k_index - 1])

        u: dict[int, float] = dict()  # µ

        for index in range(1, c.shape[0] + 1):
            if index not in b_basis_indices:
                u[index - 1] = float(np.matmul(delta_y_vector, a[:, index - 1]))
        #print("µ: ", u)

        # STEP 8 - check
        # If all µj ⩾ 0 ==> then the direct is incompatible ==> finish
        task_is_not_joint: bool = all(item >= 0 for item in list(u.values()))

        if task_is_not_joint:
            raise Exception('Problem is not joint (Задача несовместна)')

        # STEP 9
        # For each index j ∈ {1...n} which is not included in base indices and µ[j] < 0 - will calculate the following
        sigma: list[float] = []
        for index in range(1, len(c) + 1):
            if index not in b_basis_indices and u[index - 1] < 0:
                multiplication: float = float(np.matmul(a[:, index - 1], y))
                numerator: float = c[index - 1] - multiplication
                sigma_j: float = numerator / u.get(index - 1)
                sigma.append(sigma_j)
                del sigma_j
        # print('σ Sigma: ', sigma)

        # STEP 10
        # Find min(...σ), save its index
        minimum_in_sigma_array: float = min(sigma)
        j0: int = sigma.index(minimum_in_sigma_array) + 1

        # STEP 11
        # In base indices replace the k-th base index with the index j0; Then go to step 1
        b_basis_indices[j_k_index - 1] = j0


def get_pseudoplan(vector_c: np.array, basis_vector: np.array, pseudo_plan_vector: np.array) -> np.array:
    response: list[float] = [0] * len(vector_c)
    j: int = 0

    for index in basis_vector:
        response[index - 1] = pseudo_plan_vector[j]
        j += 1

    return np.array(response)
