from borb.pdf import Document
from borb.pdf import PDF
from borb.toolkit.export.html_to_pdf.html_to_pdf import HTMLToPDF


def main():

    # read entire markdown file
    html_str: str = ""
    with open("snippet_011.html", "r") as md_file_handle:
        html_str = md_file_handle.read()

    # convert
    doc: Document = HTMLToPDF.convert_html_to_pdf(html_str)
    assert doc is not None

    # write
    with open("output.pdf", "wb") as pdf_file_handle:
        PDF.dumps(pdf_file_handle, doc)


if __name__ == "__main__":
    main()
