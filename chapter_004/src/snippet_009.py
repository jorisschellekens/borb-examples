from decimal import Decimal

from borb.pdf.canvas.color.color import HexColor
from borb.pdf.canvas.layout.page_layout.page_layout import PageLayout
from borb.pdf.document.document import Document
from borb.pdf.page.page import Page
from borb.pdf.pdf import PDF


def main():

    # open document
    doc: typing.Optional[Document] = None
    with open("output_form.pdf", "rb") as pdf_file_handle:
        doc = PDF.loads(pdf_file_handle)
    assert doc is not None

    # set
    doc.get_page(0).set_form_field_value("name", "Schellekens")
    doc.get_page(0).set_form_field_value("firstname", "Joris")
    doc.get_page(0).set_form_field_value("country", "Belgium")

    # store
    with open("output_form_filled.pdf", "wb") as pdf_file_handle:
        PDF.dumps(pdf_file_handle, doc)


if __name__ == "__main__":
    main()
