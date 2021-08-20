import typing
from borb.pdf.document import Document
from borb.pdf.pdf import PDF
from borb.pdf.trailer.document_info import DocumentInfo


def main():

    doc: typing.Optional[Document] = None
    with open("output.pdf", "rb") as in_file_handle:
        doc = PDF.loads(in_file_handle)

    assert doc is not None
    document_info: DocumentInfo = doc.get_document_info()
    print("Producer: %s" % document_info.get_producer())


if __name__ == "__main__":
    main()
