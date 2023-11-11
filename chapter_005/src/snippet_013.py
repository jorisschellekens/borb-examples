import typing
from decimal import Decimal

from borb.pdf import Alignment
from borb.pdf import ConnectedShape
from borb.pdf import Document
from borb.pdf import FlexibleColumnWidthTable
from borb.pdf import LineArtFactory
from borb.pdf import PDF
from borb.pdf import Page
from borb.pdf import PageLayout
from borb.pdf import Paragraph
from borb.pdf import SingleColumnLayout
from borb.pdf.canvas.geometry.rectangle import Rectangle
from borb.toolkit import ColorExtraction


def main():

    doc: typing.Optional[Document] = None
    l: ColorExtraction = ColorExtraction()
    with open("output.pdf", "rb") as pdf_file_handle:
        doc = PDF.loads(pdf_file_handle, [l])

    # extract colors
    colors: typing.Dict[Color, Decimal] = l.get_color()[0]

    # create output Document
    doc_out: Document = Document()

    # add Page
    p: Page = Page()
    doc_out.add_page(p)

    # add PageLayout
    l: PageLayout = SingleColumnLayout(p)

    # add Paragraph
    l.add(Paragraph("These are the colors used in the input PDF:"))

    # add Table
    t: FlexibleColumnWidthTable = FlexibleColumnWidthTable(
        number_of_rows=3, number_of_columns=3, horizontal_alignment=Alignment.CENTERED
    )
    for c in colors.keys():
        t.add(
            ConnectedShape(
                LineArtFactory.droplet(
                    Rectangle(Decimal(0), Decimal(0), Decimal(32), Decimal(32))
                ),
                stroke_color=c,
                fill_color=c,
            )
        )
    t.set_padding_on_all_cells(Decimal(5), Decimal(5), Decimal(5), Decimal(5))
    t.no_borders()
    l.add(t)

    # store
    with open("output.pdf", "wb") as pdf_file_handle:
        PDF.dumps(pdf_file_handle, doc_out)


if __name__ == "__main__":
    main()
