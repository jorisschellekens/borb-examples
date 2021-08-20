import random
from pathlib import Path

from borb.io.read.types import Decimal
from borb.pdf.canvas.color.color import HexColor
from borb.pdf.canvas.font.font import Font
from borb.pdf.canvas.font.simple_font.true_type_font import TrueTypeFont
from borb.pdf.canvas.layout.emoji.emoji import Emojis
from borb.pdf.canvas.layout.layout_element import Alignment
from borb.pdf.canvas.layout.list.unordered_list import UnorderedList
from borb.pdf.canvas.layout.page_layout.multi_column_layout import SingleColumnLayout
from borb.pdf.canvas.layout.table.table import TableCell
from borb.pdf.canvas.layout.table.flexible_column_width_table import (
    FlexibleColumnWidthTable,
)
from borb.pdf.canvas.layout.text.paragraph import Paragraph
from borb.pdf.document import Document
from borb.pdf.page.page import Page
from borb.pdf.pdf import PDF


def main():

    # create document
    pdf = Document()

    # add page
    page = Page()
    pdf.append_page(page)

    layout = SingleColumnLayout(page)

    # write puzzle title
    font: Font = TrueTypeFont.true_type_font_from_file(
        Path(__file__).parent / "Pacifico-Regular.ttf"
    )
    layout.add(
        Paragraph(
            "Tents and Trees",
            font_color=HexColor("#f1cd2e"),
            font=font,
            font_size=Decimal(23),
        )
    )

    # write puzzle information
    layout.add(
        Paragraph(
            """
            You get a grid that represents a campsite. 
            There are a number of trees on the campsite. 
            You as a campsite manager must find a spot for the tent of each visitor that meets the following requirements:
            """
        )
    )
    layout.add(
        UnorderedList()
        .add(
            Paragraph(
                "A tree must be immediately next to each tent (diagonal is not allowed)."
            )
        )
        .add(
            Paragraph(
                "In total there are as many tents as trees. So every tent has its own tree."
            )
        )
        .add(
            Paragraph(
                "The numbers outside the grid indicate how many tents there are in the relevant row or column."
            )
        )
        .add(
            Paragraph(
                "Tents never touch each other: neither horizontally nor vertically nor diagonally."
            )
        )
        .add(
            Paragraph(
                "A tent can make contact with multiple trees, but is only connected to one."
            )
        )
    )

    # write grid
    w = Decimal(20)
    grid = FlexibleColumnWidthTable(
        number_of_rows=11,
        number_of_columns=11,
        margin_top=Decimal(5),
        horizontal_alignment=Alignment.CENTERED,
    )
    h_clues = [3, 2, 2, 1, 2, 2, 1, 2, 2, 3]
    v_clues = [3, 1, 1, 3, 1, 3, 2, 2, 0, 4]
    tree_layout = """
    __________
    x_____x__x
    ____x_____
    _x____x___
    ____x____x
    xx___x__x_
    ___x___x__
    _x_______x
    __x_____x_
    _x____x___
    """
    tree_layout = tree_layout.replace("\n", "").replace(" ", "")
    grid.add(
        TableCell(
            Paragraph(" "),
            preferred_height=w,
            preferred_width=w,
            border_top=False,
            border_left=False,
        )
    )
    for i in h_clues:
        grid.add(TableCell(Paragraph(str(i)), preferred_height=w, preferred_width=w))
    for i in range(0, 10):
        grid.add(
            TableCell(Paragraph(str(v_clues[i])), preferred_height=w, preferred_width=w)
        )
        for j in range(0, 10):
            if tree_layout[i * 10 + j] == "_":
                grid.add(
                    TableCell(Paragraph(" "), preferred_height=w, preferred_width=w)
                )
            else:
                grid.add(
                    TableCell(
                        random.choice(
                            [
                                Emojis.DECIDUOUS_TREE.value,
                                Emojis.EVERGREEN_TREE.value,
                            ]
                        ),
                        preferred_height=w,
                        preferred_width=w,
                    )
                )

    grid.set_padding_on_all_cells(Decimal(3), Decimal(3), Decimal(3), Decimal(3))
    layout.add(grid)

    # attempt to store PDF
    with open("showcase_004.pdf", "wb") as in_file_handle:
        PDF.dumps(in_file_handle, pdf)


if __name__ == "__main__":
    main()
