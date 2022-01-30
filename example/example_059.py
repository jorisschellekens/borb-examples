import typing
from borb.pdf.document import Document
from borb.pdf.pdf import PDF
from borb.toolkit.text.regular_expression_text_extraction import (
    RegularExpressionTextExtraction,
)


def main():

    doc: typing.Optional[Document] = None
    l: RegularExpressionTextExtraction = RegularExpressionTextExtraction(
        "[lL]orem .* [dD]olor"
    )
    with open("output.pdf", "rb") as in_file_handle:
        doc = PDF.loads(in_file_handle, [l])

    assert doc is not None
    for i, m in enumerate(l.get_matches_for_page(0)):
        print("%d %s" % (i, m.group(0)))
        for r in m.get_bounding_boxes():
            print(
                "\t%f %f %f %f" % (r.get_x(), r.get_y(), r.get_width(), r.get_height())
            )


if __name__ == "__main__":
    main()
