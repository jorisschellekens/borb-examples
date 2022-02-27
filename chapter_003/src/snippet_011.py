from decimal import Decimal

from borb.pdf.canvas.color.color import X11Color
from borb.pdf.canvas.layout.page_layout.multi_column_layout import SingleColumnLayout
from borb.pdf.canvas.layout.page_layout.page_layout import PageLayout
from borb.pdf.canvas.layout.table.fixed_column_width_table import FixedColumnWidthTable
from borb.pdf.canvas.layout.text.paragraph import Paragraph
from borb.pdf.document.document import Document
from borb.pdf.page.page import Page
from borb.pdf.pdf import PDF


def main():
    # create Document
    doc: Document = Document()

    # create Page
    page: Page = Page()

    # add Page to Document
    doc.append_page(page)

    # set a PageLayout
    layout: PageLayout = SingleColumnLayout(page)

    # create a FixedColumnWidthTable
    layout.add(
        FixedColumnWidthTable(number_of_columns=3, number_of_rows=4)
        .add(Paragraph("Lorem"))
        .add(Paragraph("Ipsum"))
        .add(Paragraph("Dolor"))
        .add(Paragraph("Sit"))
        .add(Paragraph("Amet"))
        .add(Paragraph("Consectetur"))
        .add(Paragraph("Adipiscing"))
        .add(Paragraph("Elit"))
        .add(Paragraph("Sed"))
        .add(Paragraph("Do"))
        .add(Paragraph("Eiusmod"))
        .add(Paragraph("Tempor"))
        # set padding on all (implicit) TableCell objects in the FixedColumnWidthTable
        .set_padding_on_all_cells(Decimal(2), Decimal(2), Decimal(2), Decimal(2))
        # apply 'zebra striping' to the FixedColumnWidthTable
        .even_odd_row_colors(X11Color("LightGray"), X11Color("White"))
    )

    # store
    with open("output.pdf", "wb") as out_file_handle:
        PDF.dumps(out_file_handle, doc)


if __name__ == "__main__":
    main()
