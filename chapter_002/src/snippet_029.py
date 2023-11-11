from borb.pdf import Document
from borb.pdf import Image
from borb.pdf import PDF
from borb.pdf import Page
from borb.pdf import PageLayout
from borb.pdf import SingleColumnLayout


def main():
    # create Document
    doc: Document = Document()

    # create Page
    page: Page = Page()

    # add Page to Document
    doc.add_page(page)

    # set a PageLayout
    layout: PageLayout = SingleColumnLayout(page)

    # add an Image
    #   **note** I've wrapped the code in a try/except block, so I can automatically run
    #   all snippets in this ebook. But of course, you should not do so in production-grade
    #   code
    try:
        layout.add(
            Image(
                "https://images.unsplash.com/photo-1625604029887-45f9c2f7cbc9?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8"
            )
        )
    except AssertionError as ae:
        print("borb threw an assert: %s" % str(ae))

    # store
    with open("output.pdf", "wb") as pdf_file_handle:
        PDF.dumps(pdf_file_handle, doc)


if __name__ == "__main__":
    main()
