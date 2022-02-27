from borb.pdf.document.document import Document
from borb.pdf.page.page import Page
from borb.pdf.canvas.layout.page_layout.multi_column_layout import SingleColumnLayout
from borb.pdf.canvas.layout.page_layout.page_layout import PageLayout
from borb.pdf.pdf import PDF
from borb.pdf.canvas.layout.image.image import Image
from borb.pdf.canvas.geometry.rectangle import Rectangle
from borb.pdf.canvas.layout.shape.shape import Shape
from borb.pdf.canvas.line_art.line_art_factory import LineArtFactory
from borb.pdf.canvas.color.color import X11Color

from decimal import Decimal


def main():
    # create Document
    doc: Document = Document()

    # create Page
    page: Page = Page()

    # add Page to Document
    doc.append_page(page)

    # set a PageLayout
    layout: PageLayout = SingleColumnLayout(page)

    # define size of sticky note
    r: Rectangle = Rectangle(Decimal(0), Decimal(0), Decimal(100), Decimal(100))

    # add sticky note
    layout.add(
        Shape(
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
