from borb.pdf import Document
from borb.pdf import Page


def main():

    # Create document
    pdf = Document()

    # Add page
    page = Page()
    pdf.add_page(page)


if __name__ == "__main__":
    main()
