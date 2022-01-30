import typing
from decimal import Decimal

from borb.pdf.canvas.geometry.rectangle import Rectangle
from borb.pdf.document import Document
from borb.pdf.pdf import PDF
from borb.toolkit.location.location_filter import LocationFilter
from borb.toolkit.text.simple_text_extraction import SimpleTextExtraction


def main():

    r: Rectangle = Rectangle(Decimal(280), Decimal(510), Decimal(200), Decimal(130))
    l0: LocationFilter = LocationFilter(r)
    l1: SimpleTextExtraction = SimpleTextExtraction()
    l0.add_listener(l1)

    d: typing.Optional[Document] = None
    with open("output.pdf", "rb") as pdf_file_handle:
        d = PDF.loads(pdf_file_handle, [l0])

    assert d is not None

    print(l1.get_text_for_page(0))


if __name__ == "__main__":
    main()
