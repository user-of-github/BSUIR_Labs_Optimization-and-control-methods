from data import MATRIX_A, VECTOR_C, VECTOR_X, VECTOR_B
from basic_phase_of_simplex_method import basic_phase_of_simplex_method


def main() -> None:
    response = basic_phase_of_simplex_method(MATRIX_A, VECTOR_C, VECTOR_X, VECTOR_B)

    print(response[0])


if __name__ == '__main__':
    main()
