from decimal import Decimal

from borb.pdf import Document
from borb.pdf import FixedColumnWidthTable
from borb.pdf import PDF
from borb.pdf import Page
from borb.pdf import PageLayout
from borb.pdf import Paragraph
from borb.pdf import SingleColumnLayout


def main():
    # create Document
    doc: Document = Document()

    # create Page
    page: Page = Page()

    # add Page to Document
    doc.add_page(page)

    # set a PageLayout
    layout: PageLayout = SingleColumnLayout(page)

    # create a FixedColumnWidthTable
    layout.add(
        FixedColumnWidthTable(
            number_of_columns=3,
            number_of_rows=2,
            # adjust the ratios of column widths for this FixedColumnWidthTable
            column_widths=[Decimal(2), Decimal(1), Decimal(1)],
        )
        .add(Paragraph("Lorem"))
        .add(Paragraph("Ipsum"))
        .add(Paragraph("Dolor"))
        .add(Paragraph("Sit"))
        .add(Paragraph("Amet"))
        .add(Paragraph("Consectetur"))
        # set padding on all (implicit) TableCell objects in the FixedColumnWidthTable
        .set_padding_on_all_cells(Decimal(2), Decimal(2), Decimal(2), Decimal(2))
    )

    # store
    with open("output.pdf", "wb") as out_file_handle:
        PDF.dumps(out_file_handle, doc)


if __name__ == "__main__":
    main()
