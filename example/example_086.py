from pathlib import Path

import typing
from borb.io.read.types import Decimal
from borb.pdf.canvas.color.color import HexColor
from borb.pdf.canvas.font.font import Font
from borb.pdf.canvas.font.simple_font.true_type_font import TrueTypeFont
from borb.pdf.canvas.layout.layout_element import Alignment
from borb.pdf.canvas.layout.page_layout.multi_column_layout import SingleColumnLayout
from borb.pdf.canvas.layout.table.table import TableCell
from borb.pdf.canvas.layout.table.flexible_column_width_table import (
    FlexibleColumnWidthTable,
)
from borb.pdf.canvas.layout.text.paragraph import Paragraph
from borb.pdf.document import Document
from borb.pdf.page.page import Page
from borb.pdf.page.page_size import PageSize
from borb.pdf.pdf import PDF


def main():

    # create document
    pdf = Document()

    # add page
    page = Page(PageSize.A4_LANDSCAPE.value[0], PageSize.A4_LANDSCAPE.value[1])
    pdf.append_page(page)

    layout = SingleColumnLayout(page)

    # write puzzle title
    font: Font = TrueTypeFont.true_type_font_from_file(
        Path(__file__).parent / "Pacifico-Regular.ttf"
    )
    layout.add(
        Paragraph(
            "Nonogram",
            font_color=HexColor("#f1cd2e"),
            font=font,
            font_size=Decimal(23),
        )
    )

    # write puzzle information
    layout.add(
        Paragraph(
            """
            Nonograms, also known as Paint by Numbers, Picross, Griddlers, Pic-a-Pix, and various other names, 
            are picture logic puzzles in which cells in a grid must be colored or left blank according to numbers at the side of the grid to reveal a hidden picture. 
            In this puzzle type, the numbers are a form of discrete tomography that measures how many unbroken lines of filled-in squares there are in any given row or column. 
            For example, a clue of "4 8 3" would mean there are sets of four, eight, and three filled squares, in that order, 
            with at least one blank square between successive sets.
            """
        )
    )

    # write grid
    w = Decimal(20)
    grid = FlexibleColumnWidthTable(
        number_of_rows=9,
        number_of_columns=25,
        margin_top=Decimal(12),
        horizontal_alignment=Alignment.CENTERED,
    )

    def insert_clues(cs: typing.List[int]):
        """
        This function inserts an array of clues into the table representing the nonogram.
        A clue of "0" renders an empty cell
        :param cs:  the clues to be inserted
        :return:    None
        """
        for c in cs:
            if c == 0:
                grid.add(
                    TableCell(
                        Paragraph(" "),
                        preferred_width=w,
                        preferred_height=w,
                        border_top=False,
                        border_right=False,
                        border_bottom=False,
                        border_left=False,
                    )
                )
            else:
                grid.add(
                    TableCell(
                        Paragraph(str(c), text_alignment=Alignment.CENTERED),
                        preferred_width=w,
                        preferred_height=w,
                        border_top=False,
                        border_right=False,
                        border_bottom=False,
                        border_left=False,
                    )
                )

    def insert_blanks(n: int):
        for _ in range(0, n):
            grid.add(TableCell(Paragraph(" "), preferred_width=w, preferred_height=w))

    insert_clues(
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0]
    )
    insert_clues(
        [0, 0, 0, 0, 0, 0, 0, 7, 1, 1, 2, 0, 2, 1, 1, 2, 0, 3, 1, 1, 0, 7, 1, 1, 2]
    )
    insert_clues([0, 0, 0, 0, 0, 1, 1])
    insert_blanks(18)
    insert_clues([0, 0, 0, 0, 0, 1, 1])
    insert_blanks(18)
    insert_clues([0, 0, 0, 0, 0, 1, 1])
    insert_blanks(18)
    insert_clues([0, 0, 0, 3, 2, 2, 3])
    insert_blanks(18)
    insert_clues([1, 1, 1, 1, 1, 1, 1])
    insert_blanks(18)
    insert_clues([1, 1, 1, 1, 1, 1, 1])
    insert_blanks(18)
    insert_clues([0, 0, 0, 3, 2, 1, 3])
    insert_blanks(18)

    grid.set_padding_on_all_cells(Decimal(3), Decimal(3), Decimal(3), Decimal(3))
    layout.add(grid)

    # attempt to store PDF
    with open("output.pdf", "wb") as in_file_handle:
        PDF.dumps(in_file_handle, pdf)


if __name__ == "__main__":
    main()
