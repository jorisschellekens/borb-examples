from decimal import Decimal

from borb.pdf.canvas.color.color import HexColor
from borb.pdf.canvas.layout.emoji.emoji import Emojis
from borb.pdf.canvas.layout.image.image import Image
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

    # add OrderedList of 3 objects, a Paragraph, an Image and an Emoji
    layout.add(
        OrderedList()
        .add(Paragraph("Lorem", font_color=HexColor("45CB85")))
        .add(
            Image(
                "https://images.unsplash.com/photo-1496637721836-f46d116e6d34?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8",
                width=Decimal(64),
                height=Decimal(64),
            )
        )
        .add(Emojis.PINEAPPLE.value)
    )

    # store
    with open("output.pdf", "wb") as out_file_handle:
        PDF.dumps(out_file_handle, doc)


if __name__ == "__main__":
    main()
