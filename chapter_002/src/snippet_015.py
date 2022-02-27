from borb.pdf.document.document import Document
from borb.pdf.page.page import Page
from borb.pdf.canvas.layout.page_layout.multi_column_layout import SingleColumnLayout
from borb.pdf.canvas.layout.page_layout.page_layout import PageLayout
from borb.pdf.canvas.layout.text.paragraph import Paragraph
from borb.pdf.pdf import PDF
from borb.pdf.canvas.color.color import HSVColor, HexColor
from borb.pdf.canvas.color.pantone import Pantone
from borb.pdf.canvas.layout.table.fixed_column_width_table import FixedColumnWidthTable
from borb.pdf.canvas.layout.shape.shape import Shape
from borb.pdf.canvas.line_art.line_art_factory import LineArtFactory
from borb.pdf.canvas.geometry.rectangle import Rectangle

from decimal import Decimal


def main():
    # create Document
    doc: Document = Document()

    # create Page
    page: Page = Page()

    # add Page to Document
    doc.append_page(page)

    # set a PageLayout
    layout: PageLayout = SingleColumnLayout(page)

    # generate analogous color scheme
    cs: typing.List[Color] = HSVColor.analogous(HexColor("f1cd2e"))

    # generate FixedColumnWidthTable
    t: FixedColumnWidthTable = FixedColumnWidthTable(
        number_of_rows=4, number_of_columns=3, margin_top=Decimal(12)
    )

    # add table heading
    t.add(Paragraph("Color Sample", font="Helvetica-Bold"))
    t.add(Paragraph("Hex code", font="Helvetica-Bold"))
    t.add(Paragraph("Nearest Pantone", font="Helvetica-Bold"))

    # add row for each color
    for c in cs:
        t.add(
            Shape(
                LineArtFactory.droplet(
                    Rectangle(Decimal(0), Decimal(0), Decimal(32), Decimal(32))
                ),
                stroke_color=c,
                fill_color=c,
            )
        )
        t.add(Paragraph(c.to_rgb().to_hex_string()))
        t.add(Paragraph(Pantone.find_nearest_pantone_color(c).get_name()))

    # set properties on all table cells
    t.set_padding_on_all_cells(Decimal(5), Decimal(5), Decimal(5), Decimal(5))

    # add FixedColumnWidthTable to PageLayout
    layout.add(t)

    # store
    with open("output.pdf", "wb") as pdf_file_handle:
        PDF.dumps(pdf_file_handle, doc)


if __name__ == "__main__":
    main()
