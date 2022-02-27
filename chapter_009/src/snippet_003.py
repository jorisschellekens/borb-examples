from borb.pdf.document.document import Document
from borb.pdf.page.page import Page
from borb.pdf.pdf import PDF
from borb.pdf.canvas.layout.page_layout.multi_column_layout import SingleColumnLayout
from borb.pdf.canvas.layout.page_layout.page_layout import PageLayout
from borb.pdf.canvas.layout.text.paragraph import Paragraph
from borb.pdf.canvas.color.color import HexColor
from borb.pdf.canvas.layout.table.flexible_column_width_table import (
    FlexibleColumnWidthTable,
)
from borb.pdf.canvas.layout.table.table import Table, TableCell
from borb.pdf.canvas.layout.layout_element import Alignment

from decimal import Decimal

# represent the sudoku as a plaintext str
# every . represents an empty cell in the puzzle
# this is easier to debug/change
sudoku_str: str = """
 .  6  . | 8  .  3 | .  7  . 
 .  .  1 | .  .  . | .  6  9 
 7  .  . | .  .  . | .  .  5 
---------+---------+--------
 .  .  . | 9  .  . | .  1  . 
 .  .  . | .  .  . | .  .  4 
 .  .  5 | .  1  . | .  .  . 
---------+---------+--------
 5  4  . | .  8  . | .  .  7 
 .  .  . | 5  7  . | .  .  8 
 .  9  7 | 3  .  . | .  .  . 
"""

# process sudoku_str to remove everything that is not a number or dot
for c in "\t\n|+- ":
    sudoku_str = sudoku_str.replace(c, "")


def main():

    # define theme color
    theme_color: Color = HexColor("f1cd2e")

    # create new Document
    doc: Document = Document()

    # create new Page
    page: Page = Page()
    doc.append_page(page)

    # set PageLayout
    layout: PageLayout = SingleColumnLayout(page)

    # add title to the Document
    layout.add(
        Paragraph("Sudoku Puzzle", font_color=theme_color, font_size=Decimal(20))
    )

    # add the explanation of how to solve a sudoku
    layout.add(
        Paragraph(
            """
                    Sudoku is a logic-based, combinatorial number-placement puzzle. 
                    In classic sudoku, the objective is to fill a 9×9 grid with digits so that each column, each row, 
                    and each of the nine 3×3 subgrids that compose the grid contains all of the digits from 1 to 9. 
                    The puzzle setter provides a partially completed grid, which for a well-posed puzzle has a single solution.
                    """,
            font="Helvetica-Oblique",
        )
    )

    # represent the sudoku as a table
    s: Decimal = Decimal(20)
    t: Table = FlexibleColumnWidthTable(
        number_of_rows=9, number_of_columns=9, horizontal_alignment=Alignment.CENTERED
    )
    for i in range(0, 81):
        r: int = int(i / 9)
        c: int = i % 9
        background_color: Color = HexColor("ffffff")
        if r in [0, 1, 2, 6, 7, 8] and c in [0, 1, 2, 6, 7, 8]:
            background_color = theme_color
        if r in [3, 4, 5] and c in [3, 4, 5]:
            background_color = theme_color
        if sudoku_str[i] == ".":
            t.add(
                TableCell(
                    Paragraph(" "),
                    preferred_width=s,
                    preferred_height=s,
                    background_color=background_color,
                )
            )
        else:
            t.add(
                TableCell(
                    Paragraph(sudoku_str[i], text_alignment=Alignment.CENTERED),
                    preferred_width=s,
                    preferred_height=s,
                    background_color=background_color,
                )
            )
    t.set_padding_on_all_cells(Decimal(5), Decimal(5), Decimal(5), Decimal(5))
    layout.add(t)


if __name__ == "__main__":
    main()
