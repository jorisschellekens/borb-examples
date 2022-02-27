# New imports
from borb.pdf.canvas.color.color import HexColor, X11Color


def _build_billing_and_shipping_information():
    table_001 = Table(number_of_rows=6, number_of_columns=2)
    table_001.add(
        Paragraph(
            "BILL TO",
            background_color=HexColor("263238"),
            font_color=X11Color("White"),
        )
    )
    table_001.add(
        Paragraph(
            "SHIP TO",
            background_color=HexColor("263238"),
            font_color=X11Color("White"),
        )
    )
    table_001.add(Paragraph("[Recipient Name]"))  # BILLING
    table_001.add(Paragraph("[Recipient Name]"))  # SHIPPING
    table_001.add(Paragraph("[Company Name]"))  # BILLING
    table_001.add(Paragraph("[Company Name]"))  # SHIPPING
    table_001.add(Paragraph("[Street Address]"))  # BILLING
    table_001.add(Paragraph("[Street Address]"))  # SHIPPING
    table_001.add(Paragraph("[City, State, ZIP Code]"))  # BILLING
    table_001.add(Paragraph("[City, State, ZIP Code]"))  # SHIPPING
    table_001.add(Paragraph("[Phone]"))  # BILLING
    table_001.add(Paragraph("[Phone]"))  # SHIPPING
    table_001.set_padding_on_all_cells(Decimal(2), Decimal(2), Decimal(2), Decimal(2))
    table_001.no_borders()
    return table_001
