import pprint

from get_inverse_for_matrix_with_modified_column import get_inverse_for_matrix_with_modified_column


def main() -> None:
    matrix_file_name: str = 'matrix'
    column_file_name: str = 'column'

    response = get_inverse_for_matrix_with_modified_column(matrix_file_name, column_file_name)

    if response is None:
        print('\nREVERSE MATRIX DOES NOT EXIST')
    else:
        print('\nReverse matrix is: ')
        pprint.pprint(response)


if __name__ == '__main__':
    main()
