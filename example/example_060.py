import typing
from borb.toolkit.text.font_name_filter import FontNameFilter
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
    for font_name in ["Helvetica", "Helvetica-Bold", "Courier"]:
        layout.add(Paragraph("Hello World, from %s!" % font_name, font=font_name))

    # write
    with open("output.pdf", "wb") as pdf_file_handle:
        PDF.dumps(pdf_file_handle, doc)


def extract_fonts():

    doc: typing.Optional[Document] = None
    l0: FontNameFilter = FontNameFilter("Courier")
    l1: SimpleTextExtraction = SimpleTextExtraction()
    l0.add_listener(l1)
    with open("output.pdf", "rb") as pdf_file_handle:
        doc = PDF.loads(pdf_file_handle, [l0])

    assert doc is not None

    print(l1.get_text(0))


def main():
    create_document()
    extract_fonts()


if __name__ == "__main__":
    main()
