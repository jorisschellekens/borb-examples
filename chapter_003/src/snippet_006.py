from borb.pdf import Document
from borb.pdf import PDF
from borb.pdf import Page
from borb.pdf import PageLayout
from borb.pdf import Paragraph
from borb.pdf import SingleColumnLayout
from borb.pdf import UnorderedList


def main():
    # create Document
    doc: Document = Document()

    # create Page
    page: Page = Page()

    # add Page to Document
    doc.add_page(page)

    # set a PageLayout
    layout: PageLayout = SingleColumnLayout(page)

    # add UnorderedList containing a (twice nested) UnorderedList
    layout.add(
        UnorderedList()
        .add(Paragraph("Lorem"))
        .add(Paragraph("Ipsum"))
        .add(
            UnorderedList()
            .add(Paragraph("One"))
            .add(Paragraph("Two"))
            .add(
                UnorderedList()
                .add(Paragraph("1"))
                .add(Paragraph("2"))
                .add(Paragraph("3"))
            )
            .add(Paragraph("Three"))
        )
        .add(Paragraph("Dolor"))
        .add(Paragraph("Sit"))
        .add(Paragraph("Amet"))
    )

    # store
    with open("output.pdf", "wb") as out_file_handle:
        PDF.dumps(out_file_handle, doc)


if __name__ == "__main__":
    main()
