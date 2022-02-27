import typing
from decimal import Decimal

from borb.pdf.canvas.geometry.rectangle import Rectangle
from borb.pdf.document.document import Document
from borb.pdf.pdf import PDF
from borb.toolkit.location.location_filter import LocationFilter
from borb.toolkit.text.regular_expression_text_extraction import (
    RegularExpressionTextExtraction,
    PDFMatch,
)
from borb.toolkit.text.simple_text_extraction import SimpleTextExtraction


def main():

    # set up RegularExpressionTextExtraction
    # fmt: off
    l0: RegularExpressionTextExtraction = RegularExpressionTextExtraction("[nN]isi .* aliquip")
    # fmt: on

    # process Document
    doc: typing.Optional[Document] = None
    with open("output.pdf", "rb") as in_file_handle:
        doc = PDF.loads(in_file_handle, [l0])
    assert doc is not None

    # find match
    m: typing.Optional[PDFMatch] = next(iter(l0.get_matches_for_page(0)), None)
    assert m is not None

    # get page width
    w: Decimal = doc.get_page(0).get_page_info().get_width()

    # change rectangle to get more text
    r0: Rectangle = m.get_bounding_boxes()[0]
    r1: Rectangle = Rectangle(
        r0.get_x() + r0.get_width(), r0.get_y(), w - r0.get_x(), r0.get_height()
    )

    # process document (again) filtering by rectangle
    l1: LocationFilter = LocationFilter(r1)
    l2: SimpleTextExtraction = SimpleTextExtraction()
    l1.add_listener(l2)
    doc: typing.Optional[Document] = None
    with open("output.pdf", "rb") as in_file_handle:
        doc = PDF.loads(in_file_handle, [l1])
    assert doc is not None

    # get text
    print(l2.get_text_for_page(0))


if __name__ == "__main__":
    main()
