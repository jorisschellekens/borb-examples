import typing

from borb.pdf import Document
from borb.pdf import PDF


def main():

    # load
    doc: typing.Optional[Document] = None
    with open("output.pdf", "rb") as in_file_handle:
        doc = PDF.loads(in_file_handle)

    # check whether we have read a Document
    assert doc is not None

    # print debug information for each Image (which PDF calls XObjects)
    for k, v in doc.get_page(0)["Resources"]["XObject"].items():
        print("%s\t%s" % (k, str(v)))


if __name__ == "__main__":
    main()
