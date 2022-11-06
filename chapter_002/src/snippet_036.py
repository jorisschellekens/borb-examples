from borb.pdf import Document
from borb.pdf import Page
from borb.pdf import SingleColumnLayout
from borb.pdf import PageLayout
from borb.pdf import Paragraph
from borb.pdf import PDF
from borb.pdf.canvas.layout.emoji.emoji import Emojis
from borb.pdf import ChunkOfText
from borb.pdf import InlineFlow


def main():

    # create Document
    doc: Document = Document()

    # create Page
    page: Page = Page()

    # add Page to Document
    doc.add_page(page)

    # set a PageLayout
    layout: PageLayout = SingleColumnLayout(page)
    flow: InlineFlow = InlineFlow()

    # add a Paragraph
    flow.add(ChunkOfText("Hello"))
    flow.add(Emojis.EARTH_AMERICAS.value)
    flow.add(ChunkOfText("!"))
    layout.add(flow)

    # store
    with open("output.pdf", "wb") as pdf_file_handle:
        PDF.dumps(pdf_file_handle, doc)


if __name__ == "__main__":
    main()
