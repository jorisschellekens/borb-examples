from borb.pdf import Document
from borb.pdf import Page
from borb.pdf import PageLayout
from borb.pdf import SingleColumnLayout


def main():
    # create empty Document
    pdf = Document()

    # create empty Page
    page = Page()

    # add Page to Document
    pdf.add_page(page)

    # create PageLayout
    layout: PageLayout = SingleColumnLayout(page)


if __name__ == "__main__":
    main()
