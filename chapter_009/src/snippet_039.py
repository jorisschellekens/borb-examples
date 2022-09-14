from borb.pdf import Document
from borb.pdf import Page
from borb.pdf import PDF
from borb.pdf.canvas.geometry.rectangle import Rectangle
from borb.pdf import MultiColumnLayout
from borb.pdf import PageLayout
from borb.pdf import Paragraph
from borb.pdf import HexColor
from borb.pdf.canvas.layout.image.barcode import Barcode, BarcodeType

from decimal import Decimal
from pathlib import Path


def main():

    # create Document
    doc: Document = Document()

    # create Page
    page: Page = Page()
    doc.add_page(page)

    # add javascript
    add_document_level_javascript(doc)

    # add artwork
    add_gray_artwork_to_upper_right_corner(page)
    add_colored_artwork_to_bottom_right_corner(page)

    # add Image
    add_calculator_image(page)
    add_action_annotations(page)

    # add TextField
    add_display(page)

    # create layout
    layout: PageLayout = MultiColumnLayout(page, 2)

    # add first Paragraph
    layout.add(
        Paragraph(
            "Javascript in PDF",
            font="Helvetica-Bold",
            font_size=Decimal(20),
            font_color=HexColor("56cbf9"),
        )
    )

    # add second paragraph
    layout.add(
        Paragraph(
            """
    You can cause an action to occur when a bookmark or link is clicked, or when a page is viewed. 
    For example, you can use links and bookmarks to jump to different locations in a document, 
    execute commands from a menu, and perform other actions. """
        )
    )

    # add third Paragraph
    # we are explictly adding the newlines ourselves to ensure the text
    # breaks nicely around the outline of the calculator
    layout.add(
        Paragraph(
            """To enhance the interactive qual-
    ity of a document, you can spec-
    ify actions, such as changing the 
    zoom value, to occur when a page 
    is opened or closed.""",
            respect_newlines_in_text=True,
        )
    )

    # add fourth Paragraph
    layout.add(Paragraph("Trigger Types", font="Helvetica-Bold", font_size=Decimal(14)))

    # add fifth Paragraph
    layout.add(
        Paragraph(
            "Triggers determine how actions are activated in media clips, pages, and form fields. For example, you can specify a movie or sound clip to play when a page is opened or closed. The available options depend on the specified page element."
        )
    )

    # add sixth Paragraph
    layout.add(Paragraph("Javascript", font="Helvetica-Bold", font_size=Decimal(14)))

    # add seventh Paragraph
    layout.add(
        Paragraph(
            """
    The JavaScript language was developed by Netscape Communications as a means to create interactive web pages more easily. Adobe has enhanced JavaScript so that you can easily integrate this level of interactivity into your PDF documents.
    You can invoke JavaScript code using actions associated with bookmarks, links, and pages. You can set Document Actions which lets you create document-level JavaScript actions that apply to the entire document."""
        )
    )

    # add final Paragraph
    Paragraph(
        "With enough buttons and Javascript, you could even make a functional calculator inside a PDF!",
        font="Courier",
        font_size=Decimal(8),
        padding_left=Decimal(5),
        border_left=True,
    ).paint(page, Rectangle(Decimal(350), Decimal(450), Decimal(200), Decimal(100)))

    # add QR code
    Barcode(
        "https://www.borb-pdf.com",
        type=BarcodeType.QR,
        width=Decimal(64),
        height=Decimal(64),
    ).paint(
        page, Rectangle(Decimal(595 - 64 - 15), Decimal(84), Decimal(64), Decimal(64))
    )

    # store PDF
    with open(Path("output.pdf"), "wb") as pdf_file_handle:
        PDF.dumps(pdf_file_handle, doc)
