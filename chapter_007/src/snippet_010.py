from borb.pdf import Document
from borb.pdf import PDF
from borb.toolkit.export.markdown_to_pdf.markdown_to_pdf import MarkdownToPDF

from pathlib import Path

def main():

    # read entire markdown file
    markdown_str: str = ""
    with open(Path(__file__).parent / "snippet_010.md", "r") as md_file_handle:
        markdown_str = md_file_handle.read()

    # convert
    doc: Document = MarkdownToPDF.convert_markdown_to_pdf(markdown_str)
    assert doc is not None

    # write
    with open("output.pdf", "wb") as pdf_file_handle:
        PDF.dumps(pdf_file_handle, doc)


if __name__ == "__main__":
    main()
