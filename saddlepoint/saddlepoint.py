def get_column(array: list, column_number: int) -> list:
    column = [row[column_number] for row in array]
    return column


def find_saddlepoints(array: list) -> list:
    saddlepoints = []
    for row_enum in enumerate(array):
        row_number = row_enum[0]
        row = row_enum[1]
        for column_enum in enumerate(row):
            column_number = column_enum[0]
            column = get_column(array, column_number)
            value = row[column_number]
            if value == max(row) and value == min(column):
                saddlepoints.append(tuple([row_number, column_number]))

    return saddlepoints
