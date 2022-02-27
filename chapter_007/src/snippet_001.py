from decimal import Decimal

import typing
from borb.pdf.canvas.color.color import HexColor, X11Color
from borb.pdf.canvas.layout.layout_element import Alignment
from borb.pdf.canvas.layout.page_layout.multi_column_layout import SingleColumnLayout
from borb.pdf.canvas.layout.page_layout.page_layout import PageLayout
from borb.pdf.canvas.layout.table.table import TableCell
from borb.pdf.canvas.layout.table.flexible_column_width_table import (
    FlexibleColumnWidthTable,
)
from borb.pdf.canvas.layout.table.table import Table
from borb.pdf.canvas.layout.text.paragraph import Paragraph
from borb.pdf.document.document import Document
from borb.pdf.page.page import Page
from borb.pdf.pdf import PDF


def main():

    # create empty Document
    d: Document = Document()

    # add Page
    p: Page = Page()
    d.append_page(p)

    # create PageLayout
    l: PageLayout = SingleColumnLayout(p)

    # create Table
    l.add(
        FlexibleColumnWidthTable(number_of_rows=3, number_of_columns=3)
        .add(
            TableCell(
                Paragraph(
                    "1",
                    font_color=HexColor("f1cd2e"),
                    horizontal_alignment=Alignment.RIGHT,
                ),
                row_span=3,
                preferred_width=Decimal(64),
            )
        )
        .add(TableCell(Paragraph("2")))
        .add(TableCell(Paragraph("3")))
        .add(
            TableCell(
                Paragraph(
                    "4",
                    font_color=HexColor("56cbf9"),
                    horizontal_alignment=Alignment.LEFT,
                ),
                row_span=2,
                preferred_width=Decimal(32),
            )
        )
        .add(TableCell(Paragraph("5")))
        .add(TableCell(Paragraph("6", font_color=HexColor("de6449"))))
        .set_padding_on_all_cells(Decimal(5), Decimal(5), Decimal(5), Decimal(5))
    )

    # store
    with open("output.pdf", "wb") as pdf_file_handle:
        PDF.dumps(pdf_file_handle, d)


if __name__ == "__main__":
    main()
