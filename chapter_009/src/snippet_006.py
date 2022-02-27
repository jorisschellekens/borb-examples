from borb.pdf.document.document import Document
from borb.pdf.page.page import Page

# New imports
from borb.pdf.canvas.layout.page_layout.multi_column_layout import SingleColumnLayout
from borb.pdf.canvas.layout.page_layout.page_layout import PageLayout
from decimal import Decimal


def main():

    # Create document
    pdf = Document()

    # Add page
    page = Page()
    pdf.append_page(page)

    # create PageLayout
    page_layout: PageLayout = SingleColumnLayout(page)
    page_layout.vertical_margin = page.get_page_info().get_height() * Decimal(0.02)


if __name__ == "__main__":
    main()
