# 7 Heuristics for PDF documents

Most of what you've done so far is exact.
There is an exact algorithm for retrieving the bytes of an embedded file.
There are algorithms for retrieving text that have been proven to work (for many years, in many libraries).

This section deals with some of the more "guesswork"-based algorithms for PDF.

One of these (and perhaps the most useful even) is extracting structured content: tables.

In this section you'll learn how to:

- Extract tables from a PDF
- Apply OCR to a PDF (and extracting text from the subsequent `Document`)
- Export a PDF to various image formats
- Export certain formats (HTML, Markdown) to PDF

![enter image description here](https://raw.githubusercontent.com/jorisschellekens/borb-examples/master/chapter_007/img/chapter_illustration.jpg)

{pagebreak}

## 7.1 Extracting tables from a PDF

For the next example you'll first need to create a `Document` with a `Table`.
In order to provide `borb` with a challenge, let's create a `Table` with:

- `row_span`
- `col_span`
- `font_color`
- `text_alignment`

```python
#!chapter_007/src/snippet_001.py
from decimal import Decimal

import typing
from borb.pdf.canvas.color.color import HexColor, X11Color
from borb.pdf.canvas.layout.layout_element import Alignment
from borb.pdf.canvas.layout.page_layout.multi_column_layout import SingleColumnLayout
from borb.pdf.canvas.layout.page_layout.page_layout import PageLayout
from borb.pdf.canvas.layout.table.table import TableCell
from borb.pdf.canvas.layout.table.flexible_column_width_table import (
    FlexibleColumnWidthTable,
)
from borb.pdf.canvas.layout.table.table import Table
from borb.pdf.canvas.layout.text.paragraph import Paragraph
from borb.pdf.document.document import Document
from borb.pdf.page.page import Page
from borb.pdf.pdf import PDF


def main():

    # create empty Document
    d: Document = Document()

    # add Page
    p: Page = Page()
    d.add_page(p)

    # create PageLayout
    l: PageLayout = SingleColumnLayout(p)

    # create Table
    l.add(
        FlexibleColumnWidthTable(number_of_rows=3, number_of_columns=3)
        .add(
            TableCell(
                Paragraph(
                    "1",
                    font_color=HexColor("f1cd2e"),
                    horizontal_alignment=Alignment.RIGHT,
                ),
                row_span=3,
                preferred_width=Decimal(64),
            )
        )
        .add(TableCell(Paragraph("2")))
        .add(TableCell(Paragraph("3")))
        .add(
            TableCell(
                Paragraph(
                    "4",
                    font_color=HexColor("56cbf9"),
                    horizontal_alignment=Alignment.LEFT,
                ),
                row_span=2,
                preferred_width=Decimal(32),
            )
        )
        .add(TableCell(Paragraph("5")))
        .add(TableCell(Paragraph("6", font_color=HexColor("de6449"))))
        .set_padding_on_all_cells(Decimal(5), Decimal(5), Decimal(5), Decimal(5))
    )

    # store
    with open("output.pdf", "wb") as pdf_file_handle:
        PDF.dumps(pdf_file_handle, d)


if __name__ == "__main__":
    main()
```

This creates a PDF that looks like this:

![enter image description here](https://raw.githubusercontent.com/jorisschellekens/borb-examples/master/chapter_007/img/snippet_001.png)

Now you can use the `TableDetectionByLines` implementation of `EventListener` to get the job done.

In this example, you'll be adding rectangular annotations to display the detected `Table` and `TableCell` objects.
This is something I do a lot, adding annotations is a quick and easy way to debug a PDF workflow.

```python
#!chapter_007/src/snippet_002.py
from decimal import Decimal

import typing
from borb.pdf.canvas.color.color import HexColor, X11Color
from borb.pdf.canvas.layout.layout_element import Alignment
from borb.pdf.canvas.layout.page_layout.multi_column_layout import SingleColumnLayout
from borb.pdf.canvas.layout.page_layout.page_layout import PageLayout
from borb.pdf.canvas.layout.table.table import TableCell
from borb.pdf.canvas.layout.table.flexible_column_width_table import (
    FlexibleColumnWidthTable,
)
from borb.pdf.canvas.layout.table.table import Table
from borb.pdf.canvas.layout.text.paragraph import Paragraph
from borb.pdf.document.document import Document
from borb.pdf.page.page import Page
from borb.pdf.pdf import PDF
from borb.toolkit.table.table_detection_by_lines import TableDetectionByLines
from borb.pdf.canvas.layout.annotation.square_annotation import SquareAnnotation


def main():

    doc: typing.Optional[Document] = None
    l: TableDetectionByLines = TableDetectionByLines()
    with open("output.pdf", "rb") as pdf_file_handle:
        doc = PDF.loads(pdf_file_handle, [l])

    assert doc is not None

    # get page
    p: Page = doc.get_page(0)

    # get Table(s)
    tables: typing.List[Table] = l.get_tables_for_page(0)
    assert len(tables) > 0

    for r in l.get_table_bounding_boxes_for_page(0):
        r = r.grow(Decimal(5))
        p.add_annotation(SquareAnnotation(r, stroke_color=X11Color("Green")))

    for t in tables:

        # add one annotation around each cell
        for c in t._content:
            r = c.get_bounding_box()
            r = r.shrink(Decimal(5))
            p.add_annotation(SquareAnnotation(r, stroke_color=X11Color("Red")))

    # write
    with open("output.pdf", "wb") as pdf_file_handle:
        PDF.dumps(pdf_file_handle, doc)


if __name__ == "__main__":
    main()
```

![enter image description here](https://raw.githubusercontent.com/jorisschellekens/borb-examples/master/chapter_007/img/snippet_002.png)

As you can see, `borb` was able to find the `Table` and retrieve its `TableCell` objects.
Now that you have their coordinates, you can easily use some of the earlier examples (filtering text by location for instance) to retrieve the contents of each cell.

{pagebreak}

## 7.2 Performing OCR on a PDF

This is by far one of the most classic questions on any programming-forum, or helpdesk: "My document does not seem to have text in it. Help?" or "Your text-extraction code sample does not work for my document. How come?"

The answer is often as straightforward as "your scanner hates you".

Most of the documents for which this doesn't work are PDF documents that are essentially glorified images.
They contain all the meta-data needed to constitute a PDF, but their pages are just large (often low-quality) images.

As a consequence, there are no text-rendering instructions in these documents. 
And most PDF libraries will not be able to handle them.

`borb` however is different, `borb` just loves to help.

In this section you'll be using a special `EventListener` implementation called `OCRAsOptionalContentGroup`.
This class uses `tesseract` (or rather `pytesseract`) to perform OCR (optical character recognition) on the `Document`.

Once finished, the recognized text is re-inserted in each `Page` as a special "layer" (in PDF this is called an "optional content group").

With the content now restored, the usual tricks (`SimpleTextExtraction`) yield the expected results.


You'll start by creating a method that builds a PIL `Image` with some text in it.
This `Image` will then be inserted in a PDF.

```python
#!chapter_007/src/snippet_003.py
import typing
from pathlib import Path

from borb.pdf.pdf import PDF
from PIL import Image as PILImage  # type: ignore [import]
from PIL import ImageDraw, ImageFont


def create_image() -> PILImage:

    # create new Image
    img = PILImage.new("RGB", (256, 256), color=(255, 255, 255))

    # create ImageFont
    # CAUTION: you may need to adjust the path to your particular font directory
    font = ImageFont.truetype("/usr/share/fonts/truetype/ubuntu/UbuntuMono-B.ttf", 24)

    # draw text
    draw = ImageDraw.Draw(img)
    draw.text((10, 10), "Hello World!", fill=(0, 0, 0), font=font)

    # return
    return img
```

Now you can build a `Document` with this `Image`

```python
#!chapter_007/src/snippet_004.py
import typing
from pathlib import Path

from borb.pdf.canvas.layout.image.image import Image
from borb.pdf.canvas.layout.page_layout.multi_column_layout import SingleColumnLayout
from borb.pdf.canvas.layout.page_layout.page_layout import PageLayout
from borb.pdf.canvas.layout.text.paragraph import Paragraph
from borb.pdf.document.document import Document
from borb.pdf.page.page import Page
from borb.pdf.pdf import PDF
from PIL import Image as PILImage  # type: ignore [import]
from PIL import ImageDraw, ImageFont


def create_image() -> PILImage:

    # create new Image
    img = PILImage.new("RGB", (256, 256), color=(255, 255, 255))

    # create ImageFont
    # CAUTION: you may need to adjust the path to your particular font directory
    font = ImageFont.truetype("/usr/share/fonts/truetype/ubuntu/UbuntuMono-B.ttf", 24)

    # draw text
    draw = ImageDraw.Draw(img)
    draw.text((10, 10), "Hello World!", fill=(0, 0, 0), font=font)

    # return
    return img


def main():

    # create Document
    d: Document = Document()

    # create/add Page
    p: Page = Page()
    d.add_page(p)

    # set PageLayout
    l: PageLayout = SingleColumnLayout(p)

    # add Paragraph
    l.add(Paragraph("Lorem Ipsum"))

    # add Image
    l.add(Image(create_image()))

    # write
    with open("output_001.pdf", "wb") as pdf_file_handle:
        PDF.dumps(pdf_file_handle, d)


if __name__ == "__main__":
    main()
```

The document should look something like this:

![enter image description here](https://raw.githubusercontent.com/jorisschellekens/borb-examples/master/chapter_007/img/snippet_004_001.png)

When you select the text in this document, you'll see immediately that only the top line is actually text.
The rest is an `Image` with text (the `Image` you created).

![enter image description here](https://raw.githubusercontent.com/jorisschellekens/borb-examples/master/chapter_007/img/snippet_004_002.png)

Now you can apply OCR to this `Document`:

```python
#!chapter_007/src/snippet_005.py
from borb.pdf.document.document import Document
from borb.pdf.pdf import PDF
from borb.toolkit.ocr.ocr_as_optional_content_group import OCRAsOptionalContentGroup

from pathlib import Path


def main():

    # set up everything for OCR
    tesseract_data_dir: Path = Path("/home/joris/Downloads/tessdata-master/")
    assert tesseract_data_dir.exists()
    l: OCRAsOptionalContentGroup = OCRAsOptionalContentGroup(tesseract_data_dir)

    # read Document
    doc: typing.Optional[Document] = None
    with open("output_001.pdf", "rb") as pdf_file_handle:
        doc = PDF.loads(pdf_file_handle, [l])

    assert doc is not None

    # store Document
    with open("output_002.pdf", "wb") as pdf_file_handle:
        PDF.dumps(pdf_file_handle, doc)


if __name__ == "__main__":
    main()
```

![enter image description here](https://raw.githubusercontent.com/jorisschellekens/borb-examples/master/chapter_007/img/snippet_005_001.png)

You can see this created an extra layer in the PDF.
This layer is named "OCR by borb", and contains the rendering instructions `borb` re-inserted in the `Document`.

You can toggle the visibility of this layer (this can be handy when debugging).

![enter image description here](https://raw.githubusercontent.com/jorisschellekens/borb-examples/master/chapter_007/img/snippet_005_002.png)

You can see `borb` re-inserted the postscript rendering command to ensure "Hello World!" is in the `Document.
Let's hide this layer again.

Now (even with the layer hidden), you can select the text:

![enter image description here](https://raw.githubusercontent.com/jorisschellekens/borb-examples/master/chapter_007/img/snippet_005_003.png)

And if you apply `SimpleTextExtraction` now, you should be able to retrieve all the text in the `Document`.

```python
#!chapter_007/src/snippet_006.py
from borb.pdf.document.document import Document
from borb.pdf.pdf import PDF
from borb.toolkit.text.simple_text_extraction import SimpleTextExtraction


def main():

    doc: typing.Optional[Document] = None
    l: SimpleTextExtraction = SimpleTextExtraction()
    with open("output_002.pdf", "rb") as pdf_file_handle:
        doc = PDF.loads(pdf_file_handle, [l])

    print(l.get_text_for_page(0))


if __name__ == "__main__":
    main()
```

This prints:

```
Lorem Ipsum
Hello World!
```

{pagebreak}

## 7.3 Exporting PDF as a (PIL) image

Let's start by creating a PDF we can later export.
In the next example you'll be creating a PDF with different fonts, font-sizes and an image.

```python
#!chapter_007/src/snippet_007.py
from borb.pdf.document.document import Document
from borb.pdf.page.page import Page
from borb.pdf.canvas.layout.page_layout.multi_column_layout import SingleColumnLayout
from borb.pdf.canvas.layout.page_layout.page_layout import PageLayout
from borb.pdf.canvas.layout.text.paragraph import Paragraph
from borb.pdf.canvas.layout.image.image import Image
from borb.pdf.pdf import PDF

from decimal import Decimal


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
    layout.add(
        Image(
            "https://www.gutenberg.org/cache/epub/58866/pg58866.cover.medium.jpg",
            width=Decimal(200),
            height=Decimal(300),
        )
    )

    # add a Paragraph
    layout.add(
        Paragraph("1. A Fellow Traveller", font="Helvetica-bold", font_size=Decimal(20))
    )
    layout.add(
        Paragraph(
            """
    I believe that a well-known anecdote exists to the effect that a young
    writer, determined to make the commencement of his story forcible and
    original enough to catch and rivet the attention of the most blasé of
    editors, penned the following sentence:
    """
        )
    )

    # store
    with open("output.pdf", "wb") as pdf_file_handle:
        PDF.dumps(pdf_file_handle, doc)


if __name__ == "__main__":
    main()
```

![enter image description here](https://raw.githubusercontent.com/jorisschellekens/borb-examples/master/chapter_007/img/snippet_007.png)

Now let's export this as an Image.

```python
#!chapter_007/src/snippet_008.py
from borb.pdf.pdf import PDF
from borb.toolkit.export.pdf_to_jpg import PDFToJPG

from pathlib import Path


def main():
    input_file: Path = Path(__file__).parent / "output.pdf"
    PDFToJPG.convert_pdf_to_jpg(input_file, 0).save("output_page_00.jpg")


if __name__ == "__main__":
    main()
```

![enter image description here](https://raw.githubusercontent.com/jorisschellekens/borb-examples/master/chapter_007/img/snippet_008.jpg)


{pagebreak}

## 7.4 Exporting PDF as an SVG image

```python
#!chapter_007/src/snippet_009.py
from borb.pdf.pdf import PDF
from borb.toolkit.export.pdf_to_svg import PDFToSVG

from pathlib import Path


def main():
    input_file: Path = Path(__file__).parent / "output.pdf"
    PDFToSVG.convert_pdf_to_jpg(input_file, 0).save("output_page_00.svg")


if __name__ == "__main__":
    main()
```

![enter image description here](https://raw.githubusercontent.com/jorisschellekens/borb-examples/master/chapter_007/img/snippet_009.jpg)


{pagebreak}

## 7.5 Exporting Markdown as PDF

Markdown is a very convenient format (for developers and non-technical people) to provide a quick and legible lightweight formatted document.

You'll be using the following input markdown:

> \# Headings  
> To create a heading, add number signs (#) in front of a word or phrase. The number of number signs you use should correspond to the heading level. For example, to create a heading level three (\<h3\>), use three number signs (e.g., ### My Header).
>  
> \# Heading level 1  
> \#\# Heading level 2  
> \#\#\# Heading level 3  
> \#\#\#\# Heading level 4  
> \#\#\#\#\# Heading level 5  
> \#\#\#\#\#\# Heading level 6  
>
> \#\# Alternate Syntax
> Alternatively, on the line below the text, add any number of == characters for heading level 1 or -- characters for heading level 2.
>
> Heading level 1  
> \===============
>
> Heading level 2  
> \---------------
>
> \#\# Heading Best Practices  
> Markdown applications don’t agree on how to handle a missing space between the number signs (#) and the heading name. For compatibility, always put a space between the number signs and the heading name.
>
> You should also put blank lines before and after a heading for compatibility.

Using `borb`, you can transform Markdown to PDF;

```python
#!chapter_007/src/snippet_010.py
from borb.pdf.document.document import Document
from borb.pdf.pdf import PDF
from borb.toolkit.export.markdown_to_pdf.markdown_to_pdf import MarkdownToPDF


def main():

    # read entire markdown file
    markdown_str: str = ""
    with open("snippet_010.md", "r") as md_file_handle:
        markdown_str = md_file_handle.read()

    # convert
    doc: Document = MarkdownToPDF.convert_markdown_to_pdf(markdown_str)
    assert doc is not None

    # write
    with open("output.pdf", "wb") as pdf_file_handle:
        PDF.dumps(pdf_file_handle, doc)


if __name__ == "__main__":
    main()
```

This produces the following PDF;

![enter image description here](https://raw.githubusercontent.com/jorisschellekens/borb-examples/master/chapter_007/img/snippet_010.png)

{pagebreak}

## 7.6 Exporting HTML as PDF

Another wonderful format for content is HTML. 
`borb` supports basic HTML to PDF conversion. 
Keep an eye out for this functionality in the future, as new features, tags and support will be added gradually.

For this example, you'll be using the following HTML snippet:

> \<html>  
>   \<head>  
>       \<title>Lorem Ipsum\</title>  
>   \</head>  
>       \<p>  
>            Hello World!  
>       \</p>  
>    \</html>

```python
#!chapter_007/src/snippet_011.py
from borb.pdf.document.document import Document
from borb.pdf.pdf import PDF
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
```

Which ends up producing the following PDF:

![enter image description here](https://raw.githubusercontent.com/jorisschellekens/borb-examples/master/chapter_007/img/snippet_011.png)

You'll also notice (if you open this PDF in your preferred viewer) that the title of the `Document` was set to `"lorem ipsum"`.
So `borb` also processed the meta-information.

Check out the examples in the GitHub repository and the tests to find out more supported `HTML`.

{pagebreak}

## 7.7 Conclusion

{pagebreak}

