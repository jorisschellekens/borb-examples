import typing
from decimal import Decimal

from borb.pdf.canvas.geometry.rectangle import Rectangle
from borb.pdf.document.document import Document
from borb.pdf.pdf import PDF
from borb.toolkit.location.location_filter import LocationFilter
from borb.toolkit.text.simple_text_extraction import SimpleTextExtraction


def main():

    # define the Rectangle of interest
    r: Rectangle = Rectangle(Decimal(59), Decimal(740), Decimal(99), Decimal(11))

    # define SimpleTextExtraction
    l0: SimpleTextExtraction = SimpleTextExtraction()

    # apply a LocationFilter on top of SimpleTextExtraction
    l1: LocationFilter = LocationFilter(r)
    l1.add_listener(l0)

    # read the Document
    doc: typing.Optional[Document] = None
    with open("output.pdf", "rb") as in_file_handle:
        doc = PDF.loads(in_file_handle, [l1])

    # check whether we have read a Document
    assert doc is not None

    # print the text inside the Rectangle of interest
    print(l0.get_text_for_page(0))


if __name__ == "__main__":
    main()
