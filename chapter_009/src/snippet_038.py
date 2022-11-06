from borb.pdf.canvas.layout.forms.text_field import TextField


def add_display(page: "Page"):
    r0 = Rectangle(Decimal(264), Decimal(587), Decimal(65), Decimal(15))
    Shape(
        LineArtFactory.rectangle(r0),
        stroke_color=HexColor("7e838e"),
        fill_color=HexColor("7e838e"),
    ).paint(page, r0)

    r1 = Rectangle(Decimal(264), Decimal(587), Decimal(65), Decimal(15))
    display_field = TextField(value="", font_size=Decimal(13))
    display_field.paint(page, r1)
