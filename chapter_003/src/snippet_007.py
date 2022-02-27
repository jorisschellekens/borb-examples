from borb.pdf.canvas.layout.list.ordered_list import OrderedList
from borb.pdf.canvas.layout.page_layout.multi_column_layout import SingleColumnLayout
from borb.pdf.canvas.layout.page_layout.page_layout import PageLayout
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

    # add OrderedList containing a (twice nested) OrderedList
    layout.add(
        OrderedList()
        .add(Paragraph("Lorem"))
        .add(Paragraph("Ipsum"))
        .add(
            OrderedList()
            .add(Paragraph("One"))
            .add(Paragraph("Two"))
            .add(
                OrderedList()
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
