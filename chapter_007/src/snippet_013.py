import typing

from borb.pdf import Document
from borb.pdf import PDF
from borb.toolkit import SimpleFindReplace


def main():

    # attempt to read a PDF
    doc: typing.Optional[Document] = None
    with open("output.pdf", "rb") as pdf_file_handle:
        doc = PDF.loads(pdf_file_handle)

    # check whether we actually read a PDF
    assert doc is not None

    # find/replace
    doc = SimpleFindReplace.sub("Jots", "Joris", doc)

    # store
    with open("output2.pdf", "wb") as pdf_file_handle:
        PDF.dumps(pdf_file_handle, doc)


if __name__ == "__main__":
    main()
