# Coding Exercises 1 | Hello World 🙋🏼🌎

## Exercise 1
### Multiple Choice:
Which of the following classes is used to create a new page in a borb PDF document?

- [ ] `Document`
- [ ] `Page`
- [ ] `Paragraph`
- [ ] `SingleColumnLayout`

<details>
<summary>Click here to view the solution</summary>

- [ ] `Document`
- [x] `Page`
- [ ] `Paragraph`
- [ ] `SingleColumnLayout`

The `Page` class is used to create a new page in a borb PDF document. 
`Document` is the container for the pages, while `Paragraph` and `SingleColumnLayout` are used for content and layout, respectively.

</details>

## Exercise 2
### Multiple Choice:
What is the purpose of the `SingleColumnLayout` class in the example?

- [ ] To add text to the PDF.
- [ ] To save the PDF to a file.
- [ ] To define the layout of the page content.
- [ ] To create a new page in the document.

<details>
<summary>Click here to view the explanation</summary>

- [ ] To add text to the PDF.
- [ ] To save the PDF to a file.
- [x] To define the layout of the page content.
- [ ] To create a new page in the document.

The `SingleColumnLayout` class is used to define how the content is laid out on the page. It organizes elements in a single-column format.
</details>

## Exercise 3
Write a code snippet to create a PDF document with the string `Hello World!` in it

<details>
<summary>Click here to view the solution</summary>

```python
from borb.pdf import Document
from borb.pdf import Page
from borb.pdf import PageLayout, SingleColumnLayout
from borb.pdf import Paragraph

doc: Document = Document()

page: Page = Page()
doc.append_page(page)

layout: PageLayout = SingleColumnLayout(page)

layout.append_layout_element(Paragraph('Hello World!'))

PDF.save(what=d, where_to='output.pdf')
```
</details>

## Exercise 4

What is the correct function to save a PDF document in borb?

- [ ] `Document.save()`
- [ ] `PDF.save()`
- [ ] `Page.save()`
- [ ] `Layout.save()`
       
<details> 
<summary>Click here to view the explanation</summary> 

- [ ] `Document.save()`
- [x] `PDF.save()`
- [ ] `Page.save()`
- [ ] `Layout.save()`
  
The `PDF.save()` function is used to save a borb `Document` object to a file. Other options are not valid for saving.   
</details>

## Exercise 5

Modify the code snippet from Chapter 1 to create a PDF with two pages, each containing the text "Hello World!"

<details> 
<summary>Click here to view the explanation</summary> 

```python
from borb.pdf import Document
from borb.pdf import Page
from borb.pdf import PageLayout, SingleColumnLayout
from borb.pdf import Paragraph

doc: Document = Document()

for _ in range(0, 2):
       page: Page = Page()
       doc.append_page(page)

       layout: PageLayout = SingleColumnLayout(page)
       layout.append_layout_element(Paragraph('Hello World!'))

PDF.save(what=d, where_to='output.pdf')
```
</details>
