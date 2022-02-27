from borb.pdf.document.document import Document
from borb.pdf.page.page import Page


def main():

    # Create document
    pdf = Document()

    # Add page
    page = Page()
    pdf.append_page(page)


if __name__ == "__main__":
    main()
