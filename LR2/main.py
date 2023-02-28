import data
from main_simplex_method import main_simplex_method


def main() -> None:
    response = main_simplex_method(data.MATRIX_A, data.VECTOR_C, data.VECTOR_X, data.VECTOR_B)


if __name__ == '__main__':
    main()
