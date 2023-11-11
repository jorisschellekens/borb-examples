from decimal import Decimal

from borb.pdf import Document
from borb.pdf import HexColor
from borb.pdf import PDF
from borb.pdf import Page
from borb.pdf import PageLayout
from borb.pdf import Paragraph
from borb.pdf import SingleColumnLayout
from borb.pdf.canvas.geometry.rectangle import Rectangle
from borb.pdf.canvas.layout.annotation.text_annotation import TextAnnotation
from borb.pdf.canvas.layout.annotation.text_annotation import TextAnnotationIconType
from borb.pdf.page.page_size import PageSize


def main():

    doc: Document = Document()
    page: Page = Page()
    doc.add_page(page)

    layout: PageLayout = SingleColumnLayout(page)
    layout.add(
        Paragraph(
            """
                        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
                        Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
                        Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
                        Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
                        """
        )
    )

    page_width: Decimal = PageSize.A4_PORTRAIT.value[0]
    page_height: Decimal = PageSize.A4_PORTRAIT.value[1]
    s: Decimal = Decimal(100)
    page.add_annotation(
        TextAnnotation(
            Rectangle(
                page_width / Decimal(2) - s / Decimal(2),
                page_height / Decimal(2) - s / Decimal(2),
                s,
                s,
            ),
            contents="Hello World!",
            text_annotation_icon=TextAnnotationIconType.COMMENT,
            color=HexColor("f1cd2e"),
        )
    )

    with open("output.pdf", "wb") as out_file_handle:
        PDF.dumps(out_file_handle, doc)


if __name__ == "__main__":
    main()
