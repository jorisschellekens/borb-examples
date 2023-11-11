from decimal import Decimal
from pathlib import Path

import requests
from borb.pdf import Document
from borb.pdf import Image
from borb.pdf import PDF
from borb.pdf import Page
from borb.pdf import PageLayout
from borb.pdf import SingleColumnLayout


def main():
    # create Document
    doc: Document = Document()

    # create Page
    page: Page = Page()

    # add Page to Document
    doc.add_page(page)

    # set a PageLayout
    layout: PageLayout = SingleColumnLayout(page)

    # download image and store on disk
    # this is obviously not needed if you already have an image on disk
    with open("photo-1517260911058-0fcfd733702f.jpeg", "wb") as jpg_file_handle:
        jpg_file_handle.write(
            requests.get(
                "https://images.unsplash.com/photo-1517260911058-0fcfd733702f?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8",
                stream=True,
            ).content
        )

    # add an Image
    layout.add(
        Image(
            Path("photo-1517260911058-0fcfd733702f.jpeg"),
            width=Decimal(128),
            height=Decimal(128),
        )
    )

    # store
    with open("output.pdf", "wb") as pdf_file_handle:
        PDF.dumps(pdf_file_handle, doc)


if __name__ == "__main__":
    main()
