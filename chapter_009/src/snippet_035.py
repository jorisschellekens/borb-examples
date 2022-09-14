from borb.io.read.types import Name
from borb.io.read.types import String
from borb.pdf.canvas.layout.annotation.remote_go_to_annotation import (
    RemoteGoToAnnotation,
)


def add_invisible_button(r: "Rectangle", javascript: str):
    # the next line (commented out) adds a rectangular annotation with red border
    # this makes it a lot easier to debug the calculator
    # page.add_annotation(SquareAnnotation(r, stroke_color=HexColor("ff0000"), fill_color=None))
    page.add_annotation(RemoteGoToAnnotation(r, "https://www.borbpdf.com"))
    page[Name("Annots")][-1][Name("A")][Name("S")] = Name("JavaScript")
    page[Name("Annots")][-1][Name("A")][Name("JS")] = String(javascript)
