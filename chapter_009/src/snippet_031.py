import typing
import requests
from borb.pdf.canvas.font.simple_font.true_type_font import TrueTypeFont
from borb.pdf.canvas.font.font import Font
from borb.pdf.document.document import Document
from borb.pdf.page.page import Page
from borb.pdf.pdf import PDF
from borb.pdf.canvas.layout.page_layout.multi_column_layout import SingleColumnLayout
from borb.pdf.canvas.layout.page_layout.page_layout import PageLayout
from borb.pdf.canvas.layout.text.paragraph import Paragraph
from borb.pdf.canvas.color.color import HexColor
from borb.pdf.canvas.layout.table.table import TableCell

# new imports
from borb.pdf.canvas.layout.table.fixed_column_width_table import FixedColumnWidthTable
from borb.pdf.canvas.layout.layout_element import Alignment

from pathlib import Path
from decimal import Decimal

ascii_art: str = """
■...........■..
■...........■..
■■■.■■■.■■■.■■■
■.■.■.■.■...■.■
■■■.■■■.■...■■■
"""


def calculate_horizontal_and_vertical_clues():

    # trim
    global ascii_art
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
    return (
        horizontal_clues,
        max_number_of_horizontal_clues,
        vertical_clues,
        max_number_of_vertical_clues,
    )


def download_custom_font():
    with open("IndieFlower-Regular.ttf", "wb") as ffh:
        ffh.write(
            requests.get(
                "https://github.com/google/fonts/blob/main/ofl/indieflower/IndieFlower-Regular.ttf?raw=true",
                allow_redirects=True,
            ).content
        )


def empty_cell_without_borders():
    return TableCell(
        Paragraph(" "),
        border_top=False,
        border_right=False,
        border_bottom=False,
        border_left=False,
    )


def main():
    (
        horizontal_clues,
        max_number_of_horizontal_clues,
        vertical_clues,
        max_number_of_vertical_clues,
    ) = calculate_horizontal_and_vertical_clues()

    # number_of_rows, number_of_cols
    number_of_rows: int = len(horizontal_clues)
    number_of_cols: int = int(len(ascii_art) / number_of_rows)

    download_custom_font()

    # create empty Document
    pdf = Document()

    # create empty Page
    page = Page()

    # add Page to Document
    pdf.append_page(page)

    # create PageLayout
    layout: PageLayout = SingleColumnLayout(page)

    # add title
    layout.add(
        Paragraph(
            "Nonogram",
            font_color=HexColor("#19647E"),
            font=TrueTypeFont.true_type_font_from_file(Path("IndieFlower-Regular.ttf")),
            font_size=Decimal(20),
        )
    )

    # add explanation
    layout.add(
        Paragraph(
            """
    Nonograms, also known as Hanjie, Paint by Numbers, Picross, Griddlers, and Pic-a-Pix, and by various other names, 
    are picture logic puzzles in which cells in a grid must be colored or left blank according to numbers at the side of the grid to reveal a hidden picture. 
    In this puzzle type, the numbers are a form of discrete tomography that measures how many unbroken lines of filled-in squares there are in any given row or column. 
    For example, a clue of "4 8 3" would mean there are sets of four, eight, and three filled squares, in that order, with at least one blank square between successive sets.
                        """,
            font_color=HexColor("#28AFB0"),
        )
    )

    # build table to represent nonogram
    table: FixedColumnWidthTable = FixedColumnWidthTable(
        number_of_rows=max_number_of_vertical_clues + number_of_rows,
        number_of_columns=max_number_of_horizontal_clues + number_of_cols,
    )

    for i in range(0, max_number_of_vertical_clues):
        for _ in range(0, max_number_of_horizontal_clues):
            table.add(empty_cell_without_borders())
        for j in range(0, len(vertical_clues)):
            if vertical_clues[j][i] is None:
                table.add(empty_cell_without_borders())
            else:
                table.add(
                    TableCell(
                        Paragraph(
                            str(vertical_clues[j][i]),
                            horizontal_alignment=Alignment.CENTERED,
                        ),
                        border_top=False,
                        border_right=False,
                        border_bottom=False,
                        border_left=False,
                    )
                )

    for i in range(0, len(horizontal_clues)):
        for j in horizontal_clues[i]:
            if j is None:
                table.add(empty_cell_without_borders())
            else:
                table.add(
                    TableCell(
                        Paragraph(str(j), horizontal_alignment=Alignment.CENTERED),
                        border_top=False,
                        border_right=False,
                        border_bottom=False,
                        border_left=False,
                    )
                )
        for _ in range(0, number_of_cols):
            table.add(Paragraph(" "))

    table.set_padding_on_all_cells(Decimal(2), Decimal(2), Decimal(2), Decimal(2))

    # add Table
    layout.add(table)

    # write Document
    with open("output.pdf", "wb") as pdf_file_handle:
        PDF.dumps(pdf_file_handle, pdf)


if __name__ == "__main__":
    main()
