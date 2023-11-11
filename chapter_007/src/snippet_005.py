from pathlib import Path

from borb.pdf import Document
from borb.pdf import PDF
from borb.toolkit.ocr.ocr_as_optional_content_group import OCRAsOptionalContentGroup


def main():

    # set up everything for OCR
    tesseract_data_dir: Path = Path("/home/joris/Downloads/tessdata-master/")
    assert tesseract_data_dir.exists()
    l: OCRAsOptionalContentGroup = OCRAsOptionalContentGroup(tesseract_data_dir)

    # read Document
    doc: typing.Optional[Document] = None
    with open("output_001.pdf", "rb") as pdf_file_handle:
        doc = PDF.loads(pdf_file_handle, [l])

    assert doc is not None

    # store Document
    with open("output_002.pdf", "wb") as pdf_file_handle:
        PDF.dumps(pdf_file_handle, doc)


if __name__ == "__main__":
    main()
