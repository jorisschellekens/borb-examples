from decimal import Decimal

from borb.pdf.canvas.color.color import X11Color
from borb.pdf.canvas.geometry.rectangle import Rectangle
from borb.pdf.canvas.layout.text.paragraph import Paragraph
from borb.pdf.document import Document
from borb.pdf.page.page import Page
from borb.pdf.pdf import PDF


def main():
    doc: Document = Document()
    page: Page = Page()
    doc.append_page(page)

    m: Decimal = Decimal(5)

    p: Paragraph = Paragraph(
        "Hello World!",
        # margin
        margin_top=m,
        margin_left=m,
        margin_bottom=m,
        margin_right=m,
        # padding
        padding_top=m,
        padding_left=m,
        padding_bottom=m,
        padding_right=m,
        # border
        border_top=True,
        border_right=True,
        border_bottom=True,
        border_left=True,
        border_color=X11Color("Green"),
        border_width=Decimal(0.1),
    )

    # the next line of code uses absolute positioning
    r: Rectangle = Rectangle(
        Decimal(59),  # x: 0 + page_margin
        Decimal(848 - 84 - 100),  # y: page_height - page_margin - height_of_textbox
        Decimal(595 - 59 * 2),  # width: page_width - 2 * page_margin
        Decimal(100),
    )  # height

    # add the paragraph to the page
    page.append_square_annotation(r, stroke_color=X11Color("Red"))
    p.layout(page, r)

    with open("output.pdf", "wb") as out_file_handle:
        PDF.dumps(out_file_handle, doc)


if __name__ == "__main__":
    main()
