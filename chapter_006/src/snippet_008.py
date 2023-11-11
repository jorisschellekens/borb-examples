from decimal import Decimal

from borb.io.read.types import Name
from borb.io.read.types import String
from borb.pdf import Document
from borb.pdf import Image
from borb.pdf import PDF
from borb.pdf import Page
from borb.pdf import SingleColumnLayout
from borb.pdf.canvas.layout.annotation.remote_go_to_annotation import (
    RemoteGoToAnnotation,
)


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
        "https://images.unsplash.com/photo-1614963366795-973eb8748ebb",
        width=Decimal(128),
        height=Decimal(128),
    )
    layout.add(img)

    # create RemoteGoToAnnotation
    annot: RemoteGoToAnnotation = RemoteGoToAnnotation(
        img.get_previous_paint_box(), uri="https://www.google.com"
    )

    # modify annotation
    annot[Name("A")][Name("S")] = Name("JavaScript")
    annot[Name("A")][Name("JS")] = String("app.alert('Hello World!', 3)")
    page.add_annotation(annot)

    # attempt to store PDF
    with open("output.pdf", "wb") as out_file_handle:
        PDF.dumps(out_file_handle, pdf)


if __name__ == "__main__":
    main()
