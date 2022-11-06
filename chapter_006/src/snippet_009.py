import typing
from borb.pdf import Document
from borb.pdf import PDF
from borb.pdf.canvas.geometry.rectangle import Rectangle
from borb.pdf import SingleColumnLayout
from borb.pdf import PageLayout
from borb.pdf import Page
from borb.pdf import Image
from borb.pdf.canvas.layout.annotation.sound_annotation import SoundAnnotation
from decimal import Decimal


def main():

    # create document
    pdf = Document()

    # add page
    page = Page()
    pdf.add_page(page)

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
    page.add_annotation(
        SoundAnnotation(
            img.get_previous_paint_box(), "/home/joris/Downloads/audioclip.mp3"
        )
    )

    # attempt to store PDF
    with open("output.pdf", "wb") as out_file_handle:
        PDF.dumps(out_file_handle, pdf)


if __name__ == "__main__":
    main()
