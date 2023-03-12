import pprint
from data import MATRIX_A, VECTOR_B, VECTOR_C
from start_phase_of_simplex_method import start_phase_of_simplex_method


def main() -> None:
    response = start_phase_of_simplex_method(MATRIX_A, VECTOR_B, VECTOR_C)



if __name__ == '__main__':
    main()
