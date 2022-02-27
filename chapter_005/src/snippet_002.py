import typing
from borb.pdf.document.document import Document
from borb.pdf.pdf import PDF


def main():

    # read the Document
    doc: typing.Optional[Document] = None
    with open("output.pdf", "rb") as in_file_handle:
        doc = PDF.loads(in_file_handle)

    # check whether we have read a Document
    assert doc is not None

    # print the \Author key from the \Info dictionary
    print("Author: %s" % doc.get_document_info().get_author())


if __name__ == "__main__":
    main()
