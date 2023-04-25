from dual_simplex_method import dual_simplex_method
from data import C_VECTOR, B_VECTOR, B_INDICES_BASE, A_MATRIX


def main() -> None:
    solution = dual_simplex_method(A_MATRIX, B_VECTOR, B_INDICES_BASE, C_VECTOR)
    print('Dual simplex method: ', solution)


if __name__ == '__main__':
    main()

