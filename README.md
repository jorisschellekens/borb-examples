# 1 `borb` in action

![enter image description here](img/undraw_growth_curve.png)

<div style="page-break-before: always;"></div>

## 1.1 About this book

This book will take you on an exploratory journey through the PDF format, and the `borb` Python library. You'll learn, through examples, how to use `borb` to generate and manipulate PDFs, and extract information from them. The deep-dive chapters will help you gain a thorough understanding of various interesting algorithms, or pieces of the PDF specification. The showcase examples are typically aimed at working out a use-case from start to finish.

## 1.2 About the author

![enter image description here](img/jsc_portrait.jpg)

I'm Joris Schellekens, the author of both this book and the `borb` library.
I've been a software engineer/architect for most of my professional career.
I started out working in C++ and Java, and only late in the game did I switch to Python.

I love mathematical optimization, and graph-theory. I never thought I'd be the author of a library for writing PDF documents, but here we are. Working with PDF has offered me many challenges that were often as difficult as they were satisfying to solve.

<div style="page-break-before: always;"></div>

## 1.3 Who should read this book?

This book is intended for python developers who'd like to create, or work with (existing) PDF documents. This can be anything from generating reports, invoices, to itemized inventory overviews. This book assumes you have some background in Python programming. 

This book includes a lot of small code-snippets that handle a particular facet or problem in a PDF-workflow:

- Adding `Paragraph`, `List`, `Table`, `Image` and more to a PDF document
- Adding annotations to an existing document
- Applying OCR to an existing document
- Applying redaction to an existing document
- Creating PDF documents from scratch
- Merging and splitting existing PDF documents
- Retrieving text from a document
- Etc

For the sake of completeness, most of these examples are standalone python scripts. If you want to deploy these examples in a bigger framework (as part of a web application, a document server, etc), you should know how to perform all the needed setup. This book will only explain the PDF-related parts.

No prior knowledge about PDF is needed, as this book will get into the nitty gritty details wherever needed. These sections will be clearly marked, so you can choose whether you'd like to get your head smashed in by the PDF-spec.

I would recommend the PDF-spec (ISO-32000) to anyone craving a particular brand of masochism.

<div style="page-break-before: always;"></div>

## 1.4 How to use this book

The large sections of this book are meant to stand alone. It is perfectly conceivable that you only wish to create PDF documents, and not work with existing ones, or vice-versa. You can read the book thematically, only touching chapters that are tangent to your requirements.

Of course, in order to gain a deeper understanding of the `borb` library, and PDF, 
I would recommend you read this book in its entirety, even if you only give certain sections a cursory glance.
There is so much information in this book, not just about `borb` but PDF in general. I have no doubt you'll learn something new in each section.

<div style="page-break-before: always;"></div>

## 1.5 What you'll be able to do after reading this book

This book is organized into eleven main sections:

1. **Hello World**
   This is the classic 'Hello World' example, in `borb`. Study it, type it out, memorize it. It's the basis, and it will come back time and again in the other examples.

2. **Adding Text to a PDF**  
   We’ll begin with the basics: adding text to a PDF. This includes exploring various fonts, colors, borders, and other formatting options.

3. **Working with Images and Specialized Layout Elements**  
   Once you're comfortable with text, we’ll move on to images and related `LayoutElement`s like `Barcode`, `QRCode`, `Avatar`, and more.

4. **Using Shapes and Line-Art**  
   Next, we’ll dive into `Shape` objects for creating line-art. We’ll also cover some specialized classes derived from shapes, such as `Map` and `ProgressBar`.

5. **Making interactive PDFs using FormElements**
   In this section we'll create interactive PDF documents using forms.

6. **Combining Layout Elements with Containers**  
   After understanding individual elements, we’ll focus on combining them. You’ll learn about containers, starting with lists (e.g., `OrderedList`, `UnOrderedList`) and culminating with tables (`FlexibleColumnWidthTable`, `FixedColumnWidthTable`).

7. **Using SmartArt to easily generate stunning visuals**
   In this section we'll create visuals using `SmartArt`.
   
8. **Exploring Advanced Layouts**  
   So far, we’ve used `SingleColumnLayout` to position elements. This section introduces alternative options, including `MultiColumnLayout` and freeform layouts, for greater flexibility.

9. **Using Templates for Streamlined Design**  
   If you’re less concerned with the precise placement or style of content, templates can help. We’ll introduce templates like Invoice, Slideshow, Resume, and more for faster document creation.

10. **Showcases**

11. **Processing Existing PDF Documents**  
   Finally, you’ll learn how to work with existing PDFs. This chapter covers extracting text, filtering content by colors or other criteria, and manipulating documents efficiently.

By the end, you’ll have a solid understanding of creating and processing PDFs with a variety of tools and techniques!

### 1.5.1 Hello World

### 1.5.2 Adding Text to a PDF

We’ll begin with the basics of working with text in PDFs. Adding text is a fundamental task that forms the foundation for many document creations. In this section, you will learn how to:

- **Insert Text:** Discover how to add simple text to a PDF, including setting the text's position on the page and managing its alignment (left, center, right, justified).

- **Fonts:** Explore the various font options available, such as built-in system fonts or custom fonts, and learn how to embed fonts in your PDFs to ensure they display correctly across different systems. Dive into text styling—adjusting the size, weight (bold), style (italic), and decoration (underline, strike-through) to match your document's needs.

- **Text Color:** Learn how to modify the color of your text to match your design scheme. We'll cover how to use RGB, CMYK, or named color values, and how to achieve visually appealing contrasts.

- **Borders and Backgrounds:** Understand how to add borders around text or apply backgrounds. You'll learn about different types of borders (e.g., solid, dashed) and the effect of various background fills, such as gradient colors or patterns.

- **Text Alignment and Spacing:** Explore how to adjust text alignment, line spacing, and paragraph spacing for better readability and visual appeal.

- **Text Overflow and Truncation:** Understand what happens when your text overflows the defined area and how to handle it (e.g., truncating text or automatically resizing).

By the end of this section, you’ll have the knowledge to add and style text in a variety of ways, making your PDFs visually engaging and professionally formatted.

### 1.5.3 Working with Images and Specialized Layout Elements

Once you’re comfortable with adding and styling text, it’s time to enrich your PDFs with images and other dynamic layout elements. In this section, you will explore how to:

- **Inserting Images**: Learn how to insert images into your PDFs, whether they are static files (e.g., JPEG, PNG, GIF) or vector formats (e.g., SVG). You'll also cover how to scale and position images effectively within the layout.

- **Barcode Generation**: Dive into generating barcodes within your PDFs. Learn how to create and format different types of barcodes, such as QR codes, UPC codes, and DataMatrix codes, with options for adjusting the size, color, and alignment.

- **QR Codes**: QR codes are widely used for storing URLs, text, or other small pieces of data that can be scanned by mobile devices. This section covers how to generate and place QR codes within your PDFs, ensuring they are easily readable by scanners.

- **Avatar Images**: Avatars are commonly used for profile pictures or to represent a person or entity. You’ll learn how to incorporate avatar images into your PDFs and customize them, including resizing, rounding corners, and adding borders for a polished look.

- **Image Borders and Effects**: Learn how to add styling effects to images, such as borders, shadows, or rounded corners. You can apply these effects to enhance the appearance of images and blend them seamlessly into the document’s overall design.

By the end of this section, you’ll be well-versed in adding and manipulating images in various ways, as well as incorporating advanced elements like barcodes, QR codes, and avatars, allowing you to create rich, interactive, and visually appealing PDF documents.

### 1.5.4 Using Shapes and Line-Art

In this section, we will focus on using shapes to create line-art and other graphic elements within your PDFs. You’ll learn how to work with basic shapes and explore some specialized derived classes for more complex designs. Topics covered include:

- **Basic Shapes**: Learn how to create basic shapes like lines, rectangles, circles, and polygons. These shapes can be used for everything from simple dividers to complex illustrations.

- **Shape Styling**: Understand how to style shapes with options for setting the line thickness, color, dash style (solid, dotted, dashed), and fill color. You’ll also explore transparency and opacity settings for added design flexibility.

- **Creating Line-Art**: Using the basic shape objects, you can create detailed line-art illustrations. Learn how to combine multiple shapes to create more complex visuals, such as icons, logos, and simple drawings.

- **Progress Bars**: Progress bars are a common use of shapes in PDF documents, particularly for visualizing completion or progress. You’ll learn how to generate and customize progress bars, including their style, color, and dimensions.

- **Maps**: Maps are another example of a specialized shape-derived class. This section covers how to generate and customize maps within your PDFs, whether they are static or contain interactive elements.

By the end of this section, you’ll have the skills to use shapes for creating intricate line-art and other graphic elements in your PDFs. You’ll also be able to work with specialized derived classes like ProgressBar and Map, which enhance your document's interactivity and visual appeal.


### 1.5.5 Using FormField objects to create interactive PDF documents

### 1.5.6 Combining Layout Elements with Containers

After mastering individual elements, it’s time to explore how to combine them effectively using containers. This section will teach you how to use containers like lists and tables to organize and structure content within your PDFs. Key topics include:

- **Lists**: Learn how to group content into lists for better organization. We’ll cover different types of lists, including:
  - **OrderedList**: Create numbered lists where the order of items matters. You can customize the numbering style (e.g., Arabic numerals, letters, or Roman numerals).
  - **UnOrderedList**: Create bulleted lists where the order of items does not matter. You’ll learn how to choose different bullet styles (e.g., dots, squares, etc.).
  - **RomanNumeralOrderedList**: Create ordered lists using Roman numerals (I, II, III, etc.) instead of regular numbering for a classic or formal look.

- **Tables**: Tables are powerful containers for organizing data in rows and columns. You’ll learn how to create tables using both fixed and flexible column widths:
  - **FixedColumnWidthTable**: This table type uses fixed-width columns, ensuring uniform column sizes across all rows.
  - **FlexibleColumnWidthTable**: This table type allows columns to adjust their width based on the content within them, making the layout more dynamic and responsive.
  - **Row Span**: Understand how to span a table cell across multiple rows, useful for header cells or when grouping related data.
  - **Column Span**: Learn how to span a table cell across multiple columns, enabling more complex layouts within the table.

- **Styling Tables**: Once you know how to create tables, you’ll explore how to style them:
  - **Background Colors**: Learn how to set background colors for individual cells, rows, or entire tables to make the data visually distinct and appealing.
  - **Padding**: Understand how to add padding inside table cells for better readability and to improve the overall visual spacing between the text and the cell borders.

By the end of this section, you’ll be proficient in combining various layout elements within containers such as lists and tables. You’ll have the skills to create organized, structured documents with customized list formats and well-styled, responsive tables.

### 1.5.7 SmartArt

### 1.5.8 Exploring Advanced Layouts

### 1.5.9 Using Templates for Streamlined Design

### 1.5.10 Showcases

### 1.5.11 Processing Existing PDF Documents

<div style="page-break-before: always;"></div>

## 1.6 The goal of this book

My goal for this book is for it to become a companion along your way in PDF-land. 
With this book, you'll have the answers to the most common questions, and an experienced field-guide to help you find the right tools in the `borb` library.

<div style="page-break-before: always;"></div>

## 1.7 Software requirements and downloads

`borb` is a free and open source library distributed by Joris Schellekens. You can download it from GitHub or using PyPi. The software is protected by the Affero General Public License (AGPL).

`borb` requires Python. Although no particular IDE is needed, the examples and code has been developed in PyCharm. So I can imagine there might be some bias towards this.

All examples have been tested in a Linux environment. Most of the examples are based on tests (or have inspired tests), you can download their source-code on GitHub.

### 1.7.1 Installation using `pip`

Getting started with `borb` is easy.

1. Create a virtual environment (if you have not done so already)

    `python3 -m venv venv`

2. Activate your virtual environment

    `source venv/bin/activate`
     
3. Install `borb` using pip

    `pip install borb`

4. Done :tada: You are all ready to go. 
 
Try out some of the examples to get to know `borb`.

**Note**: if you have used `borb` in the past, it's best to ensure that pip is not serving
you a version of `borb` from its cache. Uninstall your previous version using:

`pip uninstall borb`

and install the latest version using:

`pip install --no-cache borb`

<div style="page-break-before: always;"></div>

## 1.8 Acknowledgements

This book would not have been possible without Bruno Lowagie.
A sincere "thank you", to the king of PDF.

I would also like to thank (in no particular order); Daphne, Dietrich, Benoit, Michael, Diane and Aleks.
You're all awesome, and you've helped me out tremendously.

![enter image description here](img/jsc_signature.png)

<div style="page-break-before: always;"></div>
