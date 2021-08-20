from borb.pdf.canvas.layout.emoji.emoji import Emojis
from borb.pdf.canvas.layout.page_layout.browser_layout import BrowserLayout
from borb.pdf.canvas.layout.text.chunk_of_text import ChunkOfText
from borb.pdf.document import Document
from borb.pdf.page.page import Page
from borb.pdf.pdf import PDF


def main():
    doc: Document = Document()
    page: Page = Page()
    doc.append_page(page)

    layout: BrowserLayout = BrowserLayout(page)
    layout.add(ChunkOfText("Hello"))
    layout.add(Emojis.EARTH_AMERICAS.value)
    layout.add(ChunkOfText("!"))

    with open("output.pdf", "wb") as out_file_handle:
        PDF.dumps(out_file_handle, doc)


if __name__ == "__main__":
    main()
