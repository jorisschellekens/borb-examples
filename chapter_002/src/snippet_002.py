from borb.pdf import Document
from borb.pdf import Page


def main():
    # create Document
    doc: Document = Document()

    # create Page
    page: Page = Page()

    # add Page to Document
    doc.add_page(page)


if __name__ == "__main__":
    main()
