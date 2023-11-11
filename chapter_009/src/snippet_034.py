from decimal import Decimal

from borb.pdf import Image


def add_calculator_image(page: "Page"):
    calculator_img = Image(
        "https://www.shopcore.nl/pub/media/catalog/product/cache/49cebce0f131f74df9ad2e5adc64fe79/t/i/ti-1726-1.jpg",
        width=Decimal(128),
        height=Decimal(128),
    )
    calculator_img.paint(
        page,
        Rectangle(
            Decimal(595 / 2 - 128 / 2),
            Decimal(842 / 2 + 128 / 2),
            Decimal(600),
            Decimal(128),
        ),
    )
