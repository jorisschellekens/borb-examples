from decimal import Decimal

from borb.pdf import Alignment
from borb.pdf import Document
from borb.pdf import HexColor
from borb.pdf import MapOfTheWorld
from borb.pdf import PDF
from borb.pdf import Page
from borb.pdf import PageLayout
from borb.pdf import Paragraph
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

    # add some text
    layout.add(Paragraph("Olympic Summer Games Paris 2024",
                         font_size=Decimal(20),
                         font_color=HexColor("#0b5394")))
    layout.add(Paragraph("Find out all about the athletes, sports, schedules, venues, mascot and much more."))

    # add MapOfTheWorld
    layout.add(MapOfTheWorld(
            horizontal_alignment=Alignment.CENTERED,
            fill_color=HexColor("#eeeeee"),
            stroke_color=HexColor("#ffffff"),
            line_width=Decimal(0.1),
        ).set_fill_color(fill_color=HexColor("#0b5394"), key="France")
    )

    # store
    with open("output.pdf", "wb") as pdf_file_handle:
        PDF.dumps(pdf_file_handle, doc)


if __name__ == "__main__":
    main()
