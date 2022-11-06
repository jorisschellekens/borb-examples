import typing
from borb.pdf import Document
from borb.pdf import PDF

import typing
from decimal import Decimal

from borb.pdf import Document
from borb.pdf import Page
from borb.pdf import PDF
from borb.pdf import MultiColumnLayout
from borb.pdf import PageLayout
from borb.pdf import Paragraph
from borb.pdf import HexColor


def main():

    doc: typing.Optional[Document] = None
    with open("output.pdf", "rb") as pdf_file_handle:
        doc = PDF.loads(pdf_file_handle)

    assert doc is not None

    # rotate Page
    doc.get_page(0).rotate_right()

    # store Document
    with open("output.pdf", "wb") as pdf_file_handle:
        PDF.dumps(pdf_file_handle, doc)


if __name__ == "__main__":
    main()
