import typing

from borb.pdf import Document
from borb.pdf import PDF
from borb.toolkit import RegularExpressionTextExtraction


def main():

    # read the Document
    # fmt: off
    doc: typing.Optional[Document] = None
    l: RegularExpressionTextExtraction = RegularExpressionTextExtraction("[lL]orem .* [dD]olor")
    with open("output.pdf", "rb") as in_file_handle:
        doc = PDF.loads(in_file_handle, [l])
    # fmt: on

    # check whether we have read a Document
    assert doc is not None

    # print matching groups
    for i, m in enumerate(l.get_matches()[0]):
        print("%d %s" % (i, m.group(0)))
        for r in m.get_bounding_boxes():
            print(
                "\t%f %f %f %f" % (r.get_x(), r.get_y(), r.get_width(), r.get_height())
            )


if __name__ == "__main__":
    main()
