from decimal import Decimal

from borb.pdf.canvas.layout.emoji.emoji import Emojis
from borb.pdf import Alignment
from borb.pdf import SingleColumnLayout
from borb.pdf import PageLayout
from borb.pdf import TableCell
from borb.pdf import FlexibleColumnWidthTable
from borb.pdf import Paragraph
from borb.pdf import Document
from borb.pdf import Page
from borb.pdf.page.page_size import PageSize
from borb.pdf import PDF


def main():
    # create Document
    doc: Document = Document()

    # create Page
    page: Page = Page(
        width=PageSize.A4_LANDSCAPE.value[0], height=PageSize.A4_LANDSCAPE.value[1]
    )

    # add Page to Document
    doc.add_page(page)

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
