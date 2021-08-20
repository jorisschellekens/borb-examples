import typing
from borb.pdf.document import Document
from borb.pdf.pdf import PDF


def main():

    doc: typing.Optional[Document] = None
    with open("output.pdf", "rb") as in_file_handle:
        doc = PDF.loads(in_file_handle)

    assert doc is not None
    print(doc.get_document_info().get_author())


if __name__ == "__main__":
    main()
