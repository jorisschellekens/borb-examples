from decimal import Decimal

from borb.pdf import SingleColumnLayout
from borb.pdf import PageLayout
from borb.pdf import TableUtil
from borb.pdf import Paragraph
from borb.pdf import Document
from borb.pdf import Page
from borb.pdf import PDF


def main():
    # create Document
    doc: Document = Document()

    # create Page
    page: Page = Page()

    # add Page to Document
    doc.add_page(page)

    # set a PageLayout
    layout: PageLayout = SingleColumnLayout(page)

    # create a FlexibleColumnWidthTable
    layout.add(
        TableUtil.from_2d_array(
            [
                ["Language", "Number of Questions on StackOverflow"],
                ["C++", 2103930],
                ["Java", 4897157],
                ["Python", 4981167],
            ]
        )
    )

    # store
    with open("output.pdf", "wb") as out_file_handle:
        PDF.dumps(out_file_handle, doc)


if __name__ == "__main__":
    main()
