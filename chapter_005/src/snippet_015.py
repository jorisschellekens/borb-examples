import typing

from borb.pdf import Document
from borb.pdf import PDF
from borb.toolkit import FontExtraction


def main():

    # read the Document
    doc: typing.Optional[Document] = None
    l: FontExtraction = FontExtraction()
    with open("output.pdf", "rb") as in_file_handle:
        doc = PDF.loads(in_file_handle, [l])

    # check whether we have read a Document
    assert doc is not None

    # print the names of the Fonts
    print(l.get_font_names()[0])


if __name__ == "__main__":
    main()
