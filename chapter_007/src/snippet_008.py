from borb.pdf import PDF
from borb.toolkit.export.pdf_to_jpg import PDFToJPG

from pathlib import Path


def main():
    input_file: Path = Path(__file__).parent / "output.pdf"
    PDFToJPG.convert_pdf_to_jpg(input_file, 0).save("output_page_00.jpg")


if __name__ == "__main__":
    main()
