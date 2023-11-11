import typing

from borb.pdf import Document
from borb.pdf import PDF
from borb.toolkit import FontNameFilter
from borb.toolkit import SimpleTextExtraction


def main():

    # create FontNameFilter
    l0: FontNameFilter = FontNameFilter("Courier")

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
    print(l1.get_text()[0])


if __name__ == "__main__":
    main()
