from borb.pdf.pdf import PDF
from borb.toolkit.export.pdf_to_svg import PDFToSVG

from pathlib import Path


def main():
    input_file: Path = Path(__file__).parent / "output.pdf"
    PDFToSVG.convert_pdf_to_jpg(input_file, 0).save("output_page_00.svg")


if __name__ == "__main__":
    main()
