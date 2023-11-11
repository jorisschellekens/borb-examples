import typing

from borb.pdf import Document
from borb.pdf import PDF


def main():

    # read the Document
    doc: typing.Optional[Document] = None
    with open("output.pdf", "rb") as pdf_file_handle:
        doc = PDF.loads(pdf_file_handle)

    # check whether we have read a Document
    assert doc is not None

    # retrieve all embedded files and their bytes
    for k, v in doc.get_embedded_files().items():

        # display the file name, and the size
        print("%s, %d bytes" % (k, len(v)))


if __name__ == "__main__":
    main()
