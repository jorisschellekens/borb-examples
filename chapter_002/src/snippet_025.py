from decimal import Decimal

from borb.pdf import X11Color
from borb.pdf.canvas.geometry.rectangle import Rectangle
from borb.pdf import Alignment
from borb.pdf import Paragraph
from borb.pdf import Document
from borb.pdf import Page
from borb.pdf import PDF
from borb.pdf.canvas.layout.annotation.square_annotation import SquareAnnotation
from borb.pdf import HexColor


def main():

    # create Document
    doc: Document = Document()

    # create Page
    page: Page = Page()

    # add Page to Document
    doc.add_page(page)

    # define layout rectangle
    # fmt: off
    r: Rectangle = Rectangle(
        Decimal(59),  # x: 0 + page_margin
        Decimal(848 - 84 - 100),  # y: page_height - page_margin - height_of_textbox
        Decimal(595 - 59 * 2),  # width: page_width - 2 * page_margin
        Decimal(100),  # height
    )
    # fmt: on

    # this is a quick hack to easily get a rectangle on the page
    # which can be very useful for debugging
    page.add_annotation(SquareAnnotation(r, stroke_color=HexColor("#ff0000")))

    # add the paragraph to the page
    Paragraph(
        """
        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
        Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
        Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
        Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
        """,
        text_alignment=Alignment.JUSTIFIED,
    ).paint(page, r)

    with open("output.pdf", "wb") as out_file_handle:
        PDF.dumps(out_file_handle, doc)


if __name__ == "__main__":
    main()
