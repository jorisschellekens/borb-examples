import typing
from decimal import Decimal

from borb.pdf.canvas.color.color import X11Color
from borb.toolkit.text.font_color_filter import FontColorFilter
from borb.pdf.canvas.layout.page_layout.multi_column_layout import SingleColumnLayout
from borb.pdf.canvas.layout.page_layout.page_layout import PageLayout
from borb.pdf.canvas.layout.text.paragraph import Paragraph
from borb.pdf.document import Document
from borb.pdf.page.page import Page
from borb.pdf.pdf import PDF
from borb.toolkit.text.simple_text_extraction import SimpleTextExtraction


def create_document():

    # create Document
    doc: Document = Document()

    # create Page
    page: Page = Page()
    doc.append_page(page)

    # create PageLayout
    layout: PageLayout = SingleColumnLayout(page)

    # add Paragraph for each font (name)
    for font_color in [X11Color("Red"), X11Color("Green"), X11Color("Blue")]:
        layout.add(
            Paragraph(
                "Hello World, in %s!" % font_color.get_name(), font_color=font_color
            )
        )

    # write
    with open("output.pdf", "wb") as pdf_file_handle:
        PDF.dumps(pdf_file_handle, doc)


def extract_fonts():

    doc: typing.Optional[Document] = None
    l0: FontColorFilter = FontColorFilter(X11Color("Red"), Decimal(0.01))
    l1: SimpleTextExtraction = SimpleTextExtraction()
    l0.add_listener(l1)
    with open("output.pdf", "rb") as pdf_file_handle:
        doc = PDF.loads(pdf_file_handle, [l0])

    assert doc is not None

    print(l1.get_text_for_page(0))


def main():
    create_document()
    extract_fonts()


if __name__ == "__main__":
    main()
