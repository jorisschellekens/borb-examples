import typing
from pathlib import Path

from borb.pdf.pdf import PDF
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
    draw.text((10, 10), "Hello World!", fill=(0, 0, 0), font=font)

    # return
    return img
