import random
import typing
from decimal import Decimal

from borb.pdf import Document
from borb.pdf import FixedColumnWidthTable
from borb.pdf import FlexibleColumnWidthTable
from borb.pdf import HexColor
from borb.pdf import Image
from borb.pdf import Page
from borb.pdf import PageLayout
from borb.pdf import Paragraph
from borb.pdf import SingleColumnLayout
from borb.pdf import TableCell
from borb.pdf import UnorderedList
from borb.pdf.canvas.geometry.rectangle import Rectangle
from borb.pdf.canvas.layout.annotation.remote_go_to_annotation import (
    RemoteGoToAnnotation,
)
from borb.pdf.canvas.layout.image.barcode import Barcode
from borb.pdf.canvas.layout.image.barcode import BarcodeType
from borb.pdf.canvas.layout.layout_element import LayoutElement
from borb.pdf.canvas.layout.shape.connected_shape import ConnectedShape
from borb.pdf.page.page_size import PageSize


def add_gray_artwork_to_upper_right_corner(page: Page) -> None:
    """
    This method will add a gray artwork of squares and triangles in the upper right corner
    of the given Page
    """

    # define a list of gray colors
    grays: typing.List[HexColor] = [
        HexColor("A9A9A9"),
        HexColor("D3D3D3"),
        HexColor("DCDCDC"),
        HexColor("E0E0E0"),
        HexColor("E8E8E8"),
        HexColor("F0F0F0"),
    ]

    # we're going to use the size of the page later on,
    # so perhaps it's a good idea to retrieve it now
    ps: typing.Tuple[Decimal, Decimal] = PageSize.A4_PORTRAIT.value

    # now we'll write N triangles in the upper right corner
    # we'll later fill the remaining space with squares
    N: int = 4
    M: Decimal = Decimal(32)
    for i in range(0, N):
        x: Decimal = ps[0] - N * M + i * M
        y: Decimal = ps[1] - (i + 1) * M
        rg: HexColor = random.choice(grays)
        ConnectedShape(
            points=[(x + M, y), (x + M, y + M), (x, y + M)],
            stroke_color=rg,
            fill_color=rg,
        ).paint(page, Rectangle(x, y, M, M))

    # now we can fill up the remaining space with squares
    for i in range(0, N - 1):
        for j in range(0, N - 1):
            if j > i:
                continue
            x: Decimal = ps[0] - (N - 1) * M + i * M
            y: Decimal = ps[1] - (j + 1) * M
            rg: HexColor = random.choice(grays)
            ConnectedShape(
                points=[(x, y), (x + M, y), (x + M, y + M), (x, y + M)],
                stroke_color=rg,
                fill_color=rg,
            ).paint(page, Rectangle(x, y, M, M))


def main():
    # create empty Document
    pdf = Document()

    # create empty Page
    page = Page()

    # add Page to Document
    pdf.add_page(page)

    # create PageLayout
    layout: PageLayout = SingleColumnLayout(page)

    # now we can call this method in the main method
    add_gray_artwork_to_upper_right_corner(page)

    # contact information
    layout.add(
        Paragraph("Your Company", font_color=HexColor("#6d64e8"), font_size=Decimal(20))
    )

    # We're going to add a qr code that links to our website.
    # Later, we're going to add a remote go-to annotation
    # (that's just PDF talk for "if you click the qr code, it will take you to our website")
    # in order to be able to do that, we need its coordinates.
    qr_code: LayoutElement = Barcode(
        data="https://www.borbpdf.com",
        width=Decimal(64),
        height=Decimal(64),
        type=BarcodeType.QR,
    )

    # now we can add this content to the table
    layout.add(
        FlexibleColumnWidthTable(number_of_columns=2, number_of_rows=1)
        .add(qr_code)
        .add(
            Paragraph(
                """
            500 South Buena Vista Street
            Burbank CA
            91521-0991 USA
            """,
                padding_top=Decimal(12),
                respect_newlines_in_text=True,
                font_color=HexColor("#666666"),
                font_size=Decimal(10),
            )
        )
        .no_borders()
    )

    # let's add the remote go-to annotation
    page.add_annotation(
        RemoteGoToAnnotation(
            qr_code.get_previous_paint_box(), uri="https://www.borbpdf.com"
        )
    )

    # title
    layout.add(
        Paragraph(
            "Productbrochure", font_color=HexColor("#283592"), font_size=Decimal(34)
        )
    )

    # subtitle
    layout.add(
        Paragraph(
            "September 4th, 2021", font_color=HexColor("#e01b84"), font_size=Decimal(11)
        )
    )

    layout.add(
        Paragraph(
            "Product Overview", font_color=HexColor("000000"), font_size=Decimal(21)
        )
    )

    layout.add(
        Paragraph(
            """
                        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
                        Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
                        Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
                        Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
                        """
        )
    )

    # table with image and key features
    layout.add(
        FixedColumnWidthTable(
            number_of_rows=2,
            number_of_columns=2,
            column_widths=[Decimal(0.3), Decimal(0.7)],
        )
        .add(
            TableCell(
                Image(
                    "https://www.att.com/catalog/en/skus/images/apple-iphone%2012-purple-450x350.png",
                    width=Decimal(128),
                    height=Decimal(128),
                ),
                row_span=2,
            )
        )
        .add(
            Paragraph(
                "Key Features",
                font_color=HexColor("e01b84"),
                font="Helvetica-Bold",
                padding_bottom=Decimal(10),
            )
        )
        .add(
            UnorderedList()
            .add(
                Paragraph(
                    "Nam aliquet ex eget felis lobortis aliquet sit amet ut risus."
                )
            )
            .add(
                Paragraph(
                    "Maecenas sit amet odio ut erat tincidunt consectetur accumsan ut nunc."
                )
            )
            .add(Paragraph("Phasellus eget magna et justo malesuada fringilla."))
            .add(
                Paragraph(
                    "Maecenas vitae dui ac nisi aliquam malesuada in consequat sapien."
                )
            )
        )
        .no_borders()
    )


if __name__ == "__main__":
    main()
