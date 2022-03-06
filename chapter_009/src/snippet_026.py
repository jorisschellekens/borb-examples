# new imports
import typing

ascii_art: str = """
■...........■..
■...........■..
■■■.■■■.■■■.■■■
■.■.■.■.■...■.■
■■■.■■■.■...■■■
"""


def calculate_horizontal_and_vertical_clues():

    # trim
    while ascii_art[0] == "\n":
        ascii_art = ascii_art[1:]
    while ascii_art[-1] == "\n":
        ascii_art = ascii_art[:-1]

    # horizontal clues
    horizontal_clues: typing.List[typing.List[int]] = []
    for row in ascii_art.split("\n"):
        prev_char: str = ""
        prev_count: int = 0
        row_clues: typing.List[int] = []
        for c in row:
            if c == prev_char:
                prev_count += 1
            else:
                if prev_char == "■":
                    row_clues.append(prev_count)
                prev_char = c
                prev_count = 1
        if prev_char == "■":
            row_clues.append(prev_count)
        horizontal_clues.append(row_clues)
    number_of_rows: int = len(horizontal_clues)

    # vertical clues
    number_of_cols: int = int(len(ascii_art) / number_of_rows)
    vertical_clues: typing.List[typing.List[int]] = []
    for col_index in range(0, number_of_cols):
        col = [ascii_art.split("\n")[i][col_index] for i in range(0, number_of_rows)]
        prev_char: str = ""
        prev_count: int = 0
        col_clues: typing.List[int] = []
        for c in col:
            if c == prev_char:
                prev_count += 1
            else:
                if prev_char == "■":
                    col_clues.append(prev_count)
                prev_char = c
                prev_count = 1
        if prev_char == "■":
            col_clues.append(prev_count)
        vertical_clues.append(col_clues)

    # padding for horizontal_clues
    max_number_of_horizontal_clues: int = max([len(x) for x in horizontal_clues])
    for row in horizontal_clues:
        while len(row) < max_number_of_horizontal_clues:
            row.insert(0, None)

    # padding for vertical_clues
    max_number_of_vertical_clues: int = max([len(x) for x in vertical_clues])
    for col in vertical_clues:
        while len(col) < max_number_of_vertical_clues:
            col.insert(0, None)

    # return
    return horizontal_clues, vertical_clues


def main():
    pass


if __name__ == "__main__":
    main()
