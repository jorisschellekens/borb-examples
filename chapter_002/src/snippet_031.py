from decimal import Decimal

from borb.pdf import ConnectedShape
from borb.pdf import Document
from borb.pdf import PDF
from borb.pdf import Page
from borb.pdf import PageLayout
from borb.pdf import SingleColumnLayout
from borb.pdf import X11Color
from borb.pdf.canvas.geometry.rectangle import Rectangle
from borb.pdf.canvas.line_art.line_art_factory import LineArtFactory


def main():
    # create Document
    doc: Document = Document()

    # create Page
    page: Page = Page()

    # add Page to Document
    doc.add_page(page)

    # set a PageLayout
    layout: PageLayout = SingleColumnLayout(page)

    # define size of sticky note
    r: Rectangle = Rectangle(Decimal(0), Decimal(0), Decimal(100), Decimal(100))

    # add sticky note
    layout.add(
        ConnectedShape(
            LineArtFactory.sticky_note(r),
            stroke_color=X11Color("Yellow"),
            fill_color=X11Color("White"),
            line_width=Decimal(1),
        )
    )

    # store
    with open("output.pdf", "wb") as pdf_file_handle:
        PDF.dumps(pdf_file_handle, doc)


if __name__ == "__main__":
    main()
