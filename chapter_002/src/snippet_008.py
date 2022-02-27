from borb.pdf.document.document import Document
from borb.pdf.page.page import Page
from borb.pdf.canvas.layout.page_layout.multi_column_layout import SingleColumnLayout
from borb.pdf.canvas.layout.page_layout.page_layout import PageLayout
from borb.pdf.canvas.layout.text.paragraph import Paragraph
from borb.pdf.pdf import PDF
from borb.pdf.canvas.font.simple_font.true_type_font import TrueTypeFont

from pathlib import Path


def main():
    # create Document
    doc: Document = Document()

    # create Page
    page: Page = Page()

    # add Page to Document
    doc.append_page(page)

    # set a PageLayout
    layout: PageLayout = SingleColumnLayout(page)

    # construct the Font object
    font_path: Path = Path(__file__).parent / "Jsfont-Regular.ttf"
    custom_font: Font = TrueTypeFont.true_type_font_from_file(font_path)

    # add a Paragraph
    layout.add(Paragraph("Hello World!", font=custom_font))

    # store
    with open("output.pdf", "wb") as pdf_file_handle:
        PDF.dumps(pdf_file_handle, doc)


if __name__ == "__main__":
    main()
