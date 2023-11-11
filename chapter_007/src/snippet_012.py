from decimal import Decimal

from borb.pdf import Document
from borb.pdf import FixedColumnWidthTable
from borb.pdf import PDF
from borb.pdf import Page
from borb.pdf import PageLayout
from borb.pdf import Paragraph
from borb.pdf import SingleColumnLayout
from borb.pdf import Table


def main():

    # create empty Document
    doc: Document = Document()

    # add new Page
    pge: Page = Page()
    doc.add_page(pge)

    # set PageLayout
    lay: PageLayout = SingleColumnLayout(pge)

    # add Table
    tab: Table = FixedColumnWidthTable(number_of_columns=2, number_of_rows=3)
    tab.add(Paragraph("Name:", font="Helvetica-Bold"))
    tab.add(Paragraph("Schellekens"))
    tab.add(Paragraph("Firstname:", font="Helvetica-Bold"))
    tab.add(Paragraph("Jots"))
    tab.add(Paragraph("Title:", font="Helvetica-Bold"))
    tab.add(Paragraph("CEO borb"))
    tab.set_padding_on_all_cells(Decimal(5), Decimal(5), Decimal(5), Decimal(5))
    lay.add(tab)

    # store
    with open("output.pdf", 'wb') as pdf_file_handle:
        PDF.dumps(pdf_file_handle, doc)

if __name__ == "__main__":
    main()
