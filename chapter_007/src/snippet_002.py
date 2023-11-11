import typing
from decimal import Decimal

from borb.pdf import Document
from borb.pdf import PDF
from borb.pdf import Page
from borb.pdf import Table
from borb.pdf import X11Color
from borb.pdf.canvas.layout.annotation.square_annotation import SquareAnnotation
from borb.toolkit.table.table_detection_by_lines import TableDetectionByLines


def main():

    doc: typing.Optional[Document] = None
    l: TableDetectionByLines = TableDetectionByLines()
    with open("output.pdf", "rb") as pdf_file_handle:
        doc = PDF.loads(pdf_file_handle, [l])

    assert doc is not None

    # get page
    p: Page = doc.get_page(0)

    # get Table(s)
    tables: typing.List[Table] = l.get_tables()[0]
    assert len(tables) > 0

    for r in l.get_table_bounding_boxes()[0]:
        r = r.grow(Decimal(5))
        p.add_annotation(SquareAnnotation(r, stroke_color=X11Color("Green")))

    for t in tables:

        # add one annotation around each cell
        for c in t._content:
            r = c.get_previous_paint_box()
            r = r.shrink(Decimal(5))
            p.add_annotation(SquareAnnotation(r, stroke_color=X11Color("Red")))

    # write
    with open("output.pdf", "wb") as pdf_file_handle:
        PDF.dumps(pdf_file_handle, doc)


if __name__ == "__main__":
    main()
