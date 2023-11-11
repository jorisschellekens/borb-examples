import typing

from borb.pdf import Document
from borb.pdf import PDF
from borb.toolkit import ImageExtraction


def main():

    l: ImageExtraction = ImageExtraction()

    # load
    doc: typing.Optional[Document] = None
    with open("output.pdf", "rb") as in_file_handle:
        doc = PDF.loads(in_file_handle, [l])

    # check whether we have read a Document
    assert doc is not None

    print(l.get_images()[0])


if __name__ == "__main__":
    main()
