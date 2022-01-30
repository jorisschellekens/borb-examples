from pathlib import Path

from borb.io.read.types import Decimal
from borb.pdf.canvas.font.simple_font.true_type_font import TrueTypeFont
from borb.pdf.canvas.layout.horizontal_rule import HorizontalRule
from borb.pdf.canvas.layout.layout_element import Alignment
from borb.pdf.canvas.layout.page_layout.multi_column_layout import (
    SingleColumnLayout,
    MultiColumnLayout,
)
from borb.pdf.canvas.layout.page_layout.page_layout import PageLayout
from borb.pdf.canvas.layout.table.fixed_column_width_table import FixedColumnWidthTable
from borb.pdf.canvas.layout.text.paragraph import Paragraph
from borb.pdf.document import Document
from borb.pdf.page.page import Page
from borb.pdf.page.page_size import PageSize
from borb.pdf.pdf import PDF


def main():

    # create document
    pdf = Document()

    # add page
    page = Page()
    pdf.append_page(page)

    # write title
    layout_001 = SingleColumnLayout(page)
    title_table: FixedColumnWidthTable = FixedColumnWidthTable(
        number_of_rows=1,
        number_of_columns=3,
        column_widths=[Decimal(1), Decimal(4), Decimal(1)],
    )
    title_table.add(Paragraph('"All the News That\'s Fit to Print."'))
    title_table.add(
        Paragraph(
            "The New York Times",
            font_size=Decimal(26),
            text_alignment=Alignment.CENTERED,
            font="Helvetica-Bold",
        )
    )
    title_table.add(
        Paragraph(
            """
                                Today, morning clouds give way to sunshine by the afternoon high 65.
                                Tonight, cloudy low 54. 
                                Tomorrow clouds giving way to sunshine, high 70.
                                """,
            font_size=Decimal(8),
        )
    )
    title_table.no_borders()
    layout_001.add(title_table)

    layout_001.add(HorizontalRule())
    layout_001.add(Paragraph("VOL. CLXIX", text_alignment=Alignment.CENTERED))
    layout_001.add(HorizontalRule())

    # switch to MultiColumnLayout
    layout_002: PageLayout = MultiColumnLayout(page, 4)

    # mark the top section as off limits
    max_y: Decimal = Decimal(PageSize.A4_PORTRAIT.value[1] - 120)
    layout_002._page_height = max_y
    layout_002._previous_element_y = max_y - layout_002._vertical_margin

    # add content
    for _ in range(0, 10):
        layout_002.add(
            Paragraph(
                """
                                Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
                                Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
                                Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
                                Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
                                """,
                font_size=Decimal(10),
            )
        )

    # attempt to store PDF
    with open("output.pdf", "wb") as in_file_handle:
        PDF.dumps(in_file_handle, pdf)


if __name__ == "__main__":
    main()
