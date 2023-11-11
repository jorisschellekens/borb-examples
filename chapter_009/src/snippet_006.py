from decimal import Decimal

from borb.pdf import Document
from borb.pdf import Page
from borb.pdf import PageLayout
# New imports
from borb.pdf import SingleColumnLayout


def main():

    # Create document
    pdf = Document()

    # Add page
    page = Page()
    pdf.add_page(page)

    # create PageLayout
    page_layout: PageLayout = SingleColumnLayout(page)
    page_layout.vertical_margin = page.get_page_info().get_height() * Decimal(0.02)


if __name__ == "__main__":
    main()
