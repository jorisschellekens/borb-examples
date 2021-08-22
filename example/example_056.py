import typing
from decimal import Decimal

from borb.pdf.canvas.geometry.rectangle import Rectangle
from borb.pdf.document import Document
from borb.pdf.pdf import PDF
from borb.toolkit.location.location_filter import LocationFilter
from borb.toolkit.text.simple_text_extraction import SimpleTextExtraction


def main():

    doc: typing.Optional[Document] = None
    l0: SimpleTextExtraction = SimpleTextExtraction()

    r: Rectangle = Rectangle(Decimal(59), Decimal(731), Decimal(99), Decimal(11))

    l1: LocationFilter = LocationFilter(r)
    l1.add_listener(l0)

    with open("output.pdf", "rb") as in_file_handle:
        doc = PDF.loads(in_file_handle, [l1])

    assert doc is not None
    print(l0.get_text_for_page(0))


if __name__ == "__main__":
    main()
