from decimal import Decimal

from borb.pdf.canvas.layout.emoji.emoji import Emojis
from borb.pdf.canvas.layout.layout_element import Alignment
from borb.pdf.canvas.layout.page_layout.multi_column_layout import SingleColumnLayout
from borb.pdf.canvas.layout.page_layout.page_layout import PageLayout
from borb.pdf.canvas.layout.table.table import TableCell
from borb.pdf.canvas.layout.table.flexible_column_width_table import (
    FlexibleColumnWidthTable,
)
from borb.pdf.canvas.layout.text.paragraph import Paragraph
from borb.pdf.document.document import Document
from borb.pdf.page.page import Page
from borb.pdf.page.page_size import PageSize
from borb.pdf.pdf import PDF


def main():
    # create Document
    doc: Document = Document()

    # create Page
    page: Page = Page()

    # add Page to Document
    doc.append_page(page)

    # set a PageLayout
    layout: PageLayout = SingleColumnLayout(page)

    # create a FlexibleColumnWidthTable
    layout.add(
        FlexibleColumnWidthTable(number_of_columns=11, number_of_rows=5)
        # row 1
        .add(
            TableCell(
                Paragraph(" "),
                border_top=False,
                border_left=False,
            )
        )
        .add(Paragraph("View map", text_alignment=Alignment.CENTERED))
        .add(Paragraph("Place marker on a map", text_alignment=Alignment.CENTERED))
        .add(Paragraph("View direction", text_alignment=Alignment.CENTERED))
        .add(Paragraph("Launch Google maps", text_alignment=Alignment.CENTERED))
        .add(Paragraph("Show street view", text_alignment=Alignment.CENTERED))
        .add(Paragraph("Download map from Google", text_alignment=Alignment.CENTERED))
        .add(Paragraph("Show satelite view", text_alignment=Alignment.CENTERED))
        .add(
            Paragraph(
                "Search for nearest attraction", text_alignment=Alignment.CENTERED
            )
        )
        .add(Paragraph("Show next attraction", text_alignment=Alignment.CENTERED))
        .add(Paragraph("Retrieve data", text_alignment=Alignment.CENTERED))
        # row 2
        .add(Paragraph("Mobile Tourist Guide 1"))
        .add(Emojis.HEAVY_CHECK_MARK.value)
        .add(Emojis.HEAVY_CHECK_MARK.value)
        .add(Emojis.HEAVY_CHECK_MARK.value)
        .add(Emojis.HEAVY_CHECK_MARK.value)
        .add(Emojis.HEAVY_CHECK_MARK.value)
        .add(Paragraph(" "))
        .add(Paragraph(" "))
        .add(Paragraph(" "))
        .add(Paragraph(" "))
        .add(Paragraph(" "))
        # row 3
        .add(Paragraph("Mobile Tourist Guide 2"))
        .add(Emojis.HEAVY_CHECK_MARK.value)
        .add(Emojis.HEAVY_CHECK_MARK.value)
        .add(Emojis.HEAVY_CHECK_MARK.value)
        .add(Emojis.HEAVY_CHECK_MARK.value)
        .add(Emojis.HEAVY_CHECK_MARK.value)
        .add(Emojis.HEAVY_CHECK_MARK.value)
        .add(Paragraph(" "))
        .add(Paragraph(" "))
        .add(Paragraph(" "))
        .add(Paragraph(" "))
        # row 4
        .add(Paragraph("Mobile Tourist Guide 3"))
        .add(Emojis.HEAVY_CHECK_MARK.value)
        .add(Emojis.HEAVY_CHECK_MARK.value)
        .add(Emojis.HEAVY_CHECK_MARK.value)
        .add(Emojis.HEAVY_CHECK_MARK.value)
        .add(Emojis.HEAVY_CHECK_MARK.value)
        .add(Paragraph(" "))
        .add(Emojis.HEAVY_CHECK_MARK.value)
        .add(Paragraph(" "))
        .add(Paragraph(" "))
        .add(Paragraph(" "))
        # row 5
        .add(Paragraph("Mobile Tourist Guide 4"))
        .add(Emojis.HEAVY_CHECK_MARK.value)
        .add(Emojis.HEAVY_CHECK_MARK.value)
        .add(Emojis.HEAVY_CHECK_MARK.value)
        .add(Emojis.HEAVY_CHECK_MARK.value)
        .add(Emojis.HEAVY_CHECK_MARK.value)
        .add(Paragraph(" "))
        .add(Paragraph(" "))
        .add(Emojis.HEAVY_CHECK_MARK.value)
        .add(Emojis.HEAVY_CHECK_MARK.value)
        .add(Emojis.HEAVY_CHECK_MARK.value)
        .set_padding_on_all_cells(Decimal(5), Decimal(5), Decimal(5), Decimal(5))
    )

    # store
    with open("output.pdf", "wb") as out_file_handle:
        PDF.dumps(out_file_handle, doc)


if __name__ == "__main__":
    main()
