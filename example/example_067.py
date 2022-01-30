import typing
from borb.pdf.document import Document
from borb.pdf.pdf import PDF
from borb.toolkit.image.simple_image_extraction import SimpleImageExtraction


def main():

    doc: typing.Optional[Document] = None
    l: SimpleImageExtraction = SimpleImageExtraction()
    with open("output.pdf", "rb") as pdf_file_handle:
        doc = PDF.loads(pdf_file_handle, [l])

    assert doc is not None
    for img in l.get_images_for_page(0):
        print(img)


if __name__ == "__main__":
    main()
