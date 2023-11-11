from decimal import Decimal

from borb.pdf import Document
from borb.pdf import FixedColumnWidthTable
from borb.pdf import PDF
from borb.pdf import Page
from borb.pdf import PageLayout
from borb.pdf import Paragraph
from borb.pdf import ProgressBar
from borb.pdf import SingleColumnLayout


def main():

    # create Document
    doc: Document = Document()

    # create Page
    page: Page = Page()

    # add Page to Document
    doc.add_page(page)

    # set a PageLayout
    layout: PageLayout = SingleColumnLayout(page)

    # add some table
    layout.add(FixedColumnWidthTable(number_of_columns=2, number_of_rows=3)
               .add(Paragraph("TestPostscriptEval"))
               .add(ProgressBar(percentage=0.8))
               .add(Paragraph("TestDeepCopyBorbTypes"))
               .add(ProgressBar(percentage=0.88))
               .add(Paragraph("TestAddRadarPlot"))
               .add(ProgressBar(percentage=0.98))
               .set_padding_on_all_cells(Decimal(3), Decimal(3), Decimal(3), Decimal(3))
               )

    # store
    with open("output.pdf", "wb") as pdf_file_handle:
        PDF.dumps(pdf_file_handle, doc)


if __name__ == "__main__":
    main()
