from decimal import Decimal
from pathlib import Path

from borb.pdf.canvas.color.color import Color, HexColor
from borb.pdf.canvas.font.font import Font
from borb.pdf.canvas.font.simple_font.true_type_font import TrueTypeFont
from borb.pdf.canvas.layout.layout_element import Alignment
from borb.pdf.canvas.layout.page_layout.multi_column_layout import SingleColumnLayout
from borb.pdf.canvas.layout.page_layout.page_layout import PageLayout
from borb.pdf.canvas.layout.table.flexible_column_width_table import (
    FlexibleColumnWidthTable,
)
from borb.pdf.canvas.layout.table.table import Table, TableCell
from borb.pdf.canvas.layout.text.paragraph import Paragraph
from borb.pdf.document import Document
from borb.pdf.page.page import Page
from borb.pdf.pdf import PDF


def main():

    # represent the sudoku as a plaintext str
    # this is easier to debug/change
    sudoku_str: str = """
    3.9...4..
    2..7.9...
    .87......
    75..6.23.
    6..9.4..8
    .28.5..41
    ......59.
    ...1.6..7
    ..6...1.4
    """
    sudoku_str = sudoku_str.replace("\t", "").replace(" ", "").replace("\n", "")

    # create empty Document
    doc: Document = Document()

    # create empty Page
    p: Page = Page()
    doc.append_page(p)

    # create PageLayout
    l: PageLayout = SingleColumnLayout(p)

    # add Title
    pacifico: Font = TrueTypeFont.true_type_font_from_file(
        Path(__file__).parent / "Pacifico-Regular.ttf"
    )
    l.add(
        Paragraph(
            "Sudoku",
            font_size=Decimal(24),
            font_color=HexColor("0b3954"),
            font=pacifico,
        )
    )

    # add explanation
    l.add(
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

    # add Table
    s: Decimal = Decimal(20)
    t: Table = FlexibleColumnWidthTable(number_of_rows=9, number_of_columns=9)
    for i in range(0, 81):
        r: int = int(i / 9)
        c: int = i % 9
        background_color: Color = HexColor("ffffff")
        if r in [0, 1, 2, 6, 7, 8] and c in [0, 1, 2, 6, 7, 8]:
            background_color = HexColor("f1cd2e")
        if r in [3, 4, 5] and c in [3, 4, 5]:
            background_color = HexColor("f1cd2e")
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
    l.add(t)

    # store
    with open("showcase_002.pdf", "wb") as out_file_handle:
        PDF.dumps(out_file_handle, doc)


if __name__ == "__main__":
    main()
