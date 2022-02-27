import typing
from borb.pdf.document.document import Document
from borb.pdf.pdf import PDF
from borb.pdf.canvas.geometry.rectangle import Rectangle
from borb.pdf.canvas.layout.page_layout.multi_column_layout import SingleColumnLayout
from borb.pdf.canvas.layout.page_layout.page_layout import PageLayout
from borb.pdf.page.page import Page
from borb.pdf.canvas.layout.image.image import Image
from borb.pdf.canvas.layout.annotation.sound_annotation import SoundAnnotation
from decimal import Decimal


def main():

    # create document
    pdf = Document()

    # add page
    page = Page()
    pdf.append_page(page)

    # add test information
    layout = SingleColumnLayout(page)

    # add image
    img: Image = Image(
        "https://images.unsplash.com/photo-1513883049090-d0b7439799bf",
        width=Decimal(128),
        height=Decimal(128),
    )
    layout.add(img)

    # add sound annotation
    page.append_annotation(
        SoundAnnotation(img.get_bounding_box(), "/home/joris/Downloads/audioclip.mp3")
    )

    # attempt to store PDF
    with open(self.output_dir / "output.pdf", "wb") as out_file_handle:
        PDF.dumps(out_file_handle, pdf)


if __name__ == "__main__":
    main()
