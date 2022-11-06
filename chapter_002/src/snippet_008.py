from borb.pdf import Document
from borb.pdf import Page
from borb.pdf import PageLayout
from borb.pdf import SingleColumnLayout
from borb.pdf import Paragraph
from borb.pdf import PDF

# not an easy import
from borb.pdf.canvas.font.simple_font.true_type_font import TrueTypeFont

from pathlib import Path
import requests


def main():
    # create Document
    doc: Document = Document()

    # create Page
    page: Page = Page()

    # add Page to Document
    doc.add_page(page)

    # set a PageLayout
    layout: PageLayout = SingleColumnLayout(page)

    # download and store the font
    # this is obviously not needed if you already have a ttf font on disk
    font_path: Path = Path(__file__).parent / "MsMadi-Regular.ttf"
    with open(font_path, "wb") as font_file_handle:
        font_file_handle.write(
            requests.get(
                "https://github.com/google/fonts/raw/main/ofl/msmadi/MsMadi-Regular.ttf",
                stream=True,
            ).content
        )

    # construct the Font object
    font_path: Path = Path(__file__).parent / "MsMadi-Regular.ttf"
    custom_font: Font = TrueTypeFont.true_type_font_from_file(font_path)

    # add a Paragraph
    layout.add(Paragraph("Hello World!", font=custom_font))

    # store
    with open("output.pdf", "wb") as pdf_file_handle:
        PDF.dumps(pdf_file_handle, doc)


if __name__ == "__main__":
    main()
