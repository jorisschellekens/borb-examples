import xml.etree.ElementTree as ET
from pathlib import Path

from borb.pdf import PDF
from borb.toolkit.export.pdf_to_svg import PDFToSVG


def main():

    # read PDF
    input_file: Path = Path(__file__).parent / "output.pdf"
    with open(input_file, "rb") as pdf_file_handle:
        doc = PDF.loads(pdf_file_handle)

    # write ET.Element
    with open("output_page_00.svg", "wb") as svg_file_handle:
        svg_file_handle.write(ET.tostring(PDFToSVG.convert_pdf_to_svg(doc)[0]))


if __name__ == "__main__":
    main()
