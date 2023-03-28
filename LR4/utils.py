import numpy as np


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