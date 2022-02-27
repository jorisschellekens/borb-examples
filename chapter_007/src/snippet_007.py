from borb.pdf.document.document import Document
from borb.pdf.page.page import Page
from borb.pdf.canvas.layout.page_layout.multi_column_layout import SingleColumnLayout
from borb.pdf.canvas.layout.page_layout.page_layout import PageLayout
from borb.pdf.canvas.layout.text.paragraph import Paragraph
from borb.pdf.canvas.layout.image.image import Image
from borb.pdf.pdf import PDF

from decimal import Decimal


def main():
    # create Document
    doc: Document = Document()

    # create Page
    page: Page = Page()

    # add Page to Document
    doc.append_page(page)

    # set a PageLayout
    layout: PageLayout = SingleColumnLayout(page)

    # add an Image
    layout.add(
        Image(
            "https://www.gutenberg.org/cache/epub/58866/pg58866.cover.medium.jpg",
            width=Decimal(200),
            height=Decimal(300),
        )
    )

    # add a Paragraph
    layout.add(
        Paragraph("1. A Fellow Traveller", font="Helvetica-bold", font_size=Decimal(20))
    )
    layout.add(
        Paragraph(
            """
    I believe that a well-known anecdote exists to the effect that a young
    writer, determined to make the commencement of his story forcible and
    original enough to catch and rivet the attention of the most blasé of
    editors, penned the following sentence:
    """
        )
    )

    # store
    with open("output.pdf", "wb") as pdf_file_handle:
        PDF.dumps(pdf_file_handle, doc)


if __name__ == "__main__":
    main()
