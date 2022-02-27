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

    # get
    print("Name: %s" % doc.get_page(0).get_form_field_value("name"))
    print("Firstname: %s" % doc.get_page(0).get_form_field_value("firstname"))
    print("Country: %s" % doc.get_page(0).get_form_field_value("country"))


if __name__ == "__main__":
    main()
