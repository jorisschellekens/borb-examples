from borb.pdf import PDF
from borb.toolkit.export.pdf_to_jpg import PDFToJPG

from pathlib import Path


def main():

    # read PDF
    input_file: Path = Path(__file__).parent / "output.pdf"
    with open(input_file, "rb") as pdf_file_handle:
        doc = PDF.loads(pdf_file_handle)

    # convert to JPG
    PDFToJPG.convert_pdf_to_jpg(doc)[0].save("output_page_00.jpg")


if __name__ == "__main__":
    main()
