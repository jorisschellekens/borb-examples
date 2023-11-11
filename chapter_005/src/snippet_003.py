import typing

from borb.pdf import Document
from borb.pdf import PDF


def main():

    # read the Document
    doc: typing.Optional[Document] = None
    with open("output.pdf", "rb") as in_file_handle:
        doc = PDF.loads(in_file_handle)

    # check whether we have read a Document
    assert doc is not None

    # print the \Producer key from the \Info dictionary
    print("Producer: %s" % doc.get_document_info().get_producer())


if __name__ == "__main__":
    main()
