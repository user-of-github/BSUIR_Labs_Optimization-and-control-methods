from data import MATRIX_A, VECTOR_B
from start_phase_of_simplex_method import start_phase_of_simplex_method


def main() -> None:
    response = start_phase_of_simplex_method(MATRIX_A, VECTOR_B)
    print('X = ( ', response[0], ' )')
    print('B = { ', response[1], ' }')
    print('A = ( ', response[2], ' )')
    print('b = ( ', response[3], ' )')


if __name__ == '__main__':
    main()
