from borb.pdf import Document
from borb.pdf import Page
from borb.pdf import SingleColumnLayout
from borb.pdf import PageLayout
from borb.pdf import Paragraph
from borb.pdf import PDF
from borb.pdf.canvas.layout.image.unsplash import Unsplash

from decimal import Decimal
import keyring


def main():

    # set the unsplash API access key
    keyring.set_password("unsplash", "access_key", "<your access key here>")

    # create Document
    doc: Document = Document()

    # create Page
    page: Page = Page()

    # add Page to Document
    doc.add_page(page)

    # set a PageLayout
    layout: PageLayout = SingleColumnLayout(page)

    # add an Image from Unsplash
    # you can specify the keywords as well as the desired dimensions
    layout.add(Unsplash.get_image(["cherry", "blossom"], Decimal(400), Decimal(300)))

    # store
    with open("output.pdf", "wb") as pdf_file_handle:
        PDF.dumps(pdf_file_handle, doc)


if __name__ == "__main__":
    main()
