import typing
from borb.pdf import Document
from borb.pdf import PDF

from decimal import Decimal
import typing

from borb.pdf import HexColor
from borb.pdf import SingleColumnLayout
from borb.pdf import PageLayout
from borb.pdf import Paragraph
from borb.pdf import Document
from borb.pdf import Page
from borb.pdf import PDF


def main():

    d: Document = Document()

    N: int = 10
    for i in range(0, N):
        p: Page = Page()
        d.add_page(p)
        l: PageLayout = SingleColumnLayout(p)
        l.add(
            Paragraph(
                "Page %d of %d" % (i + 1, N),
                font_color=HexColor("56cbf9"),
                font_size=Decimal(24),
            )
        )
        l.add(
            Paragraph(
                """
                        Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
                        Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, 
                        when an unknown printer took a galley of type and scrambled it to make a type specimen book. 
                        It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. 
                        It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, 
                        and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
                        """,
                font_color=HexColor("f1cd2e"),
            )
        )

    with open("output_002.pdf", "wb") as pdf_out_handle:
        PDF.dumps(pdf_out_handle, d)


if __name__ == "__main__":
    main()
