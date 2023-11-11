from decimal import Decimal

from borb.pdf import Document
from borb.pdf import HSVColor
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

    # the following code generates 20 colors, evenly spaced in the HSV spectrum
    colors = [
        HSVColor(Decimal(x / 360), Decimal(1), Decimal(1))
        for x in range(0, 360, int(360 / 20))
    ]

    # add a Paragraph for each Color
    for c in colors:
        layout.add(Paragraph("Hello World!", font_color=c))

    # store
    with open("output.pdf", "wb") as pdf_file_handle:
        PDF.dumps(pdf_file_handle, doc)


if __name__ == "__main__":
    main()
