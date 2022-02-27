from borb.pdf.document.document import Document
from borb.pdf.page.page import Page
from borb.pdf.canvas.layout.page_layout.browser_layout import BrowserLayout
from borb.pdf.canvas.layout.page_layout.page_layout import PageLayout
from borb.pdf.canvas.layout.text.paragraph import Paragraph
from borb.pdf.pdf import PDF
from borb.pdf.canvas.layout.emoji.emoji import Emojis
from borb.pdf.canvas.layout.text.chunk_of_text import ChunkOfText


def main():
    # create Document
    doc: Document = Document()

    # create Page
    page: Page = Page()

    # add Page to Document
    doc.append_page(page)

    # set a PageLayout
    layout: PageLayout = BrowserLayout(page)

    # add a Paragraph
    layout.add(ChunkOfText("Hello"))
    layout.add(Emojis.EARTH_AMERICAS.value)
    layout.add(ChunkOfText("!"))

    # store
    with open("output.pdf", "wb") as pdf_file_handle:
        PDF.dumps(pdf_file_handle, doc)


if __name__ == "__main__":
    main()
