from borb.pdf import Document
from borb.pdf import Page
from borb.pdf import SingleColumnLayout
from borb.pdf import PageLayout
from borb.pdf import Paragraph
from borb.pdf import PDF
from borb.pdf import Barcode, BarcodeType
from borb.pdf import HexColor

from decimal import Decimal


def main():
    # create Document
    doc: Document = Document()

    # create Page
    page: Page = Page()

    # add Page to Document
    doc.add_page(page)

    # set a PageLayout
    layout: PageLayout = SingleColumnLayout(page)

    # add a Paragraph
    layout.add(
        Barcode(
            "1234567896120",
            width=Decimal(128),
            height=Decimal(128),
            stroke_color=HexColor("E2C044"),
            fill_color=HexColor("587B7F"),
            type=BarcodeType.EAN_14,
        )
    )

    # store
    with open("output.pdf", "wb") as pdf_file_handle:
        PDF.dumps(pdf_file_handle, doc)


if __name__ == "__main__":
    main()
