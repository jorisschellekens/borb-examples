from borb.pdf.document.document import Document
from borb.pdf.page.page import Page


def main():
    # create Document
    doc: Document = Document()

    # create Page
    page: Page = Page()

    # add Page to Document
    doc.append_page(page)


if __name__ == "__main__":
    main()
