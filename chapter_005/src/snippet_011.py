import typing

from borb.pdf import Document
from borb.pdf import PDF
from borb.toolkit import TextRankKeywordExtraction


def main():

    l: TextRankKeywordExtraction = TextRankKeywordExtraction()

    # load
    doc: typing.Optional[Document] = None
    with open("output.pdf", "rb") as in_file_handle:
        doc = PDF.loads(in_file_handle, [l])

    # check whether we have read a Document
    assert doc is not None

    print(l.get_keywords()[0])


if __name__ == "__main__":
    main()
