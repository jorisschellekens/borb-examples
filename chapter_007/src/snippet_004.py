import typing
from pathlib import Path

from borb.pdf import Image
from borb.pdf import SingleColumnLayout
from borb.pdf import PageLayout
from borb.pdf import Paragraph
from borb.pdf import Document
from borb.pdf import Page
from borb.pdf import PDF
from PIL import Image as PILImage  # type: ignore [import]
from PIL import ImageDraw, ImageFont


def create_image() -> PILImage:

    # create new Image
    img = PILImage.new("RGB", (256, 256), color=(255, 255, 255))

    # create ImageFont
    # CAUTION: you may need to adjust the path to your particular font directory
    font = ImageFont.truetype("/usr/share/fonts/truetype/ubuntu/UbuntuMono-B.ttf", 24)

    # draw text
    draw = ImageDraw.Draw(img)
    draw.fontmode = "L"
    draw.text((10, 10), "Hello World!", fill=(0, 0, 0), font=font)

    # return
    output_path: Path = Path(__file__).parent / "image_hello_world.png"
    img.save(output_path, dpi=(600, 600))
    return output_path


def main():

    # create Document
    d: Document = Document()

    # create/add Page
    p: Page = Page()
    d.add_page(p)

    # set PageLayout
    l: PageLayout = SingleColumnLayout(p)

    # add Paragraph
    l.add(Paragraph("Lorem Ipsum"))

    # add Image
    l.add(Image(create_image()))

    # write
    with open("output_001.pdf", "wb") as pdf_file_handle:
        PDF.dumps(pdf_file_handle, d)


if __name__ == "__main__":
    main()
