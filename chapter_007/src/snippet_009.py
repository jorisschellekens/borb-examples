from borb.pdf import PDF
from borb.toolkit.export.pdf_to_svg import PDFToSVG

from pathlib import Path
import xml.etree.ElementTree as ET

def main():
    input_file: Path = Path(__file__).parent / "output.pdf"

    with open("output_page_00.svg", "wb") as svg_file_handle:
        svg_file_handle.write(ET.tostring(PDFToSVG.convert_pdf_to_svg(input_file, 0)))


if __name__ == "__main__":
    main()
