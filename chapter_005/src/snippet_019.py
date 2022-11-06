import typing
from borb.pdf import Document
from borb.pdf import PDF
from borb.toolkit import FontColorFilter
from borb.toolkit import SimpleTextExtraction
from borb.pdf import X11Color

from decimal import Decimal


def main():

    # create FontColorFilter
    l0: FontColorFilter = FontColorFilter(X11Color("Red"), Decimal(0.01))

    # filtered text just gets passed to SimpleTextExtraction
    l1: SimpleTextExtraction = SimpleTextExtraction()
    l0.add_listener(l1)

    # read the Document
    doc: typing.Optional[Document] = None
    with open("output.pdf", "rb") as in_file_handle:
        doc = PDF.loads(in_file_handle, [l0])

    # check whether we have read a Document
    assert doc is not None

    # print the names of the Fonts
    print(l1.get_text_for_page(0))


if __name__ == "__main__":
    main()
