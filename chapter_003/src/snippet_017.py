from decimal import Decimal

from borb.pdf import Document
from borb.pdf import FlexibleColumnWidthTable
from borb.pdf import PDF
from borb.pdf import Page
from borb.pdf import PageLayout
from borb.pdf import Paragraph
from borb.pdf import SingleColumnLayout
from borb.pdf import TableCell


def main():
    # create Document
    doc: Document = Document()

    # create Page
    page: Page = Page()

    # add Page to Document
    doc.add_page(page)

    # set a PageLayout
    layout: PageLayout = SingleColumnLayout(page)

    # create a FlexibleColumnWidthTable
    layout.add(
        FlexibleColumnWidthTable(number_of_columns=3, number_of_rows=2)
        .add(Paragraph("Lorem"))
        .add(Paragraph("Ipsum"))
        .add(Paragraph("Dolor"))
        # set column_span to 2
        .add(TableCell(Paragraph("Sit"), column_span=2))
        .add(Paragraph("Amet"))
        .set_padding_on_all_cells(Decimal(2), Decimal(2), Decimal(2), Decimal(2))
    )

    # store
    with open("output.pdf", "wb") as out_file_handle:
        PDF.dumps(out_file_handle, doc)


if __name__ == "__main__":
    main()
