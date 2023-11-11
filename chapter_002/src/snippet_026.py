from decimal import Decimal

from borb.pdf import Document
from borb.pdf import PDF
from borb.pdf import Page
from borb.pdf import Paragraph
from borb.pdf import X11Color
from borb.pdf.canvas.geometry.rectangle import Rectangle


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
        Decimal(59),                # x: 0 + page_margin
        Decimal(848 - 84 - 100),    # y: page_height - page_margin - height_of_textbox
        Decimal(595 - 59 * 2),      # width: page_width - 2 * page_margin
        Decimal(100),               # height
    )
    # fmt: on

    # the next line of code uses absolute positioning
    Paragraph(
        "Hello World!",
        border_top=True,
        border_right=True,
        border_bottom=True,
        border_left=True,
        border_color=X11Color("Green"),
        border_width=Decimal(0.1),
    ).paint(page, r)

    # store
    with open("output.pdf", "wb") as pdf_file_handle:
        PDF.dumps(pdf_file_handle, doc)


if __name__ == "__main__":
    main()
