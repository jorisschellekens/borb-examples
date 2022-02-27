import typing
from borb.pdf.document.document import Document
from borb.pdf.pdf import PDF
from borb.toolkit.text.font_name_filter import FontNameFilter
from borb.toolkit.text.simple_text_extraction import SimpleTextExtraction


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
    print(l1.get_text_for_page(0))


if __name__ == "__main__":
    main()
