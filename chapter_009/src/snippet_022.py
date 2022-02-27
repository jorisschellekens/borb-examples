# new imports
from borb.pdf.canvas.line_art.line_art_factory import LineArtFactory


def add_colored_artwork_to_bottom_right_corner(page: Page) -> None:
    """
    This method will add a blue/purple artwork of lines and squares to the bottom right corner
    of the given Page
    """
    ps: typing.Tuple[Decimal, Decimal] = PageSize.A4_PORTRAIT.value

    # square
    Shape(
        points=[(ps[0] - 32, 40), (ps[0], 40), (ps[0], 40 + 32), (ps[0] - 32, 40 + 32)],
        stroke_color=HexColor("d53067"),
        fill_color=HexColor("d53067"),
    ).layout(page, Rectangle(ps[0] - 32, 40, 32, 32))

    # square
    Shape(
        points=[
            (ps[0] - 64, 40),
            (ps[0] - 32, 40),
            (ps[0] - 32, 40 + 32),
            (ps[0] - 64, 40 + 32),
        ],
        stroke_color=HexColor("eb3f79"),
        fill_color=HexColor("eb3f79"),
    ).layout(page, Rectangle(ps[0] - 64, 40, 32, 32))

    # triangle
    Shape(
        points=[(ps[0] - 96, 40), (ps[0] - 64, 40), (ps[0] - 64, 40 + 32)],
        stroke_color=HexColor("e01b84"),
        fill_color=HexColor("e01b84"),
    ).layout(page, Rectangle(ps[0] - 96, 40, 32, 32))

    # line
    r: Rectangle = Rectangle(Decimal(0), Decimal(32), ps[0], Decimal(8))
    Shape(
        points=LineArtFactory.rectangle(r),
        stroke_color=HexColor("283592"),
        fill_color=HexColor("283592"),
    ).layout(page, r)
