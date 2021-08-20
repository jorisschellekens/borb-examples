# Table of Contents

1. [borb in action](#1-borb-in-action)  
    1.1 [About this book](#11-about-this-book)  
    1.2 [About the author](#12-about-the-author)  
    1.3 [Who should read this book?](#13-who-should-read-this-book)  
    1.4 [How to use this book](#14-how-to-use-this-book)  
    1.5 [What you'll be able to do after reading this book](#15-what-youll-be-able-to-do-after-reading-this-book)  
        1.5.1 [Creating PDF documents](#151-creating-pdf-documents)  
        1.5.2 [Manipulate existing PDF documents](#152-manipulate-existing-pdf-documents)  
        1.5.3 [Heuristics for PDF documents](#153-heuristics-for-pdf-documents)  
        1.5.4 [Deep-dive](#154-deep-dive)  
        1.5.5 [Showcases](#155-showcases)    
    1.6 [The goal of this book](#16-the-goal-of-this-book)  
    1.7 [Software requirements and downloads](#17-software-requirements-and-downloads)  
        1.7.1 [Installation using `pip`](#171-installation-using-pip)  
    1.8 [Acknowledgements](#18-acknowledgements)
           
2. [Creating PDF documents from scratch](#2-creating-pdf-documents-from-scratch)  
    2.1 [Introducing `borb` and PDF](#21-introducing-borb-and-pdf)  
    2.2 [Steps to creating a PDF using `borb`](#22-steps-to-creating-a-pdf-using-borb)  
        2.2.1 [Creating an empty `Document` instance](#221-creating-an-empty-document-instance)  
        2.2.2 [Creating and adding a `Page`](#222-creating-and-adding-a-page)  
        2.2.3 [Setting a `PageLayout`](#223-setting-a-pagelayout)  
        2.2.4 [Adding a `Paragraph` to the `Page` using `PageLayout`](#224-adding-a-paragraph-to-the-page-using-pagelayout)    
        2.2.5 [Writing the `Document` to disk](#225-writing-the-document-to-disk)        
    2.3 [Using `LayoutElement` sub-classes to represent various types of content](#23-using-layoutelement-sub-classes-to-represent-various-types-of-content)     
    2.4 [Adding text to a PDF](#24-adding-text-to-a-pdf)  
        2.4.1 [Setting the `font` of a `Paragraph`](#241-setting-the-font-of-a-paragraph)  
        2.4.2 [Setting the `font_color` of a `Paragraph`](#242-setting-the-font_color-of-a-paragraph)  
            2.4.2.1 [Using `HSVColor` to create a rainbow of text](#2421-using-hsvcolor-to-create-a-rainbow-of-text)  
            2.4.2.2 [Using `X11Color` to specify color in a more human-legible way](#2422-using-x11color-to-specify-color-in-a-more-human-legible-way)  
            2.4.2.3 [Using `Pantone` to specify color in a more human-legible way](#2423-using-pantone-to-specify-color-in-a-more-human-legible-way)  
            2.4.2.4 [Making the most of the `Color` classes](#2424-making-the-most-of-the-color-classes)  
                2.4.2.4.1 [Generating a triad `Color` scheme](#24241-generating-a-triad-color-scheme)  
                2.4.2.4.2 [Generating a split-complementary `Color` scheme](#24242-generating-a-split-complementary-color-scheme)  
                2.4.2.4.3 [Generating an analogous `Color` scheme](#24243-generating-an-analogous-color-scheme)  
                2.4.2.4.4 [Generating a tetradic square `Color` scheme](#24244-generating-a-tetradic-square-color-scheme)  
                2.4.2.4.5 [Generating a tetradic rectangular `Color` scheme](#24245-generating-a-tetradic-rectangular-color-scheme)  
        2.4.3 [Using alignment on `Paragraph` objects](#243-using-alignment-on-paragraph-objects)  
            2.4.3.1 [`horizontal_alignment`](#2431-horizontal-alignment)  
            2.4.3.2 [`vertical_alignment`](#2432-vertical-alignment)  
            2.4.3.3 [`text_alignment`](#2433-text-alignment)  
        2.4.4 [Using borders on `Paragraph` objects](#244-using-borders-on-paragraph-objects)  
        2.4.5 [Using margin and padding on `Paragraph` objects](#245-using-margin-and-padding-on-paragraph-objects)         
    2.5 [Adding `Image` objects to a PDF](#25-adding-image-objects-to-a-pdf)      
    2.6 [Adding line-art to a PDF using `Shape` objects](#26-adding-line-art-to-a-pdf-using-shape-objects)      
    2.7 [Adding barcodes and qr-codes to a PDF](#27-adding-barcodes-and-qr-codes-to-a-pdf)  
        2.7.1 [Adding a `Barcode` to a `Page`](#271-adding-a-barcode-to-a-page)  
            2.7.1.1 [Setting the `stroke_color` and `fill_color` of a `Barcode`](#2711-setting-the-stroke_color-and-fill_color-of-a-barcode)  
        2.7.2 [Adding a QR-code to a `Page`](#272-adding-a-qr-code-to-the-page)          
    2.8 [Adding `Chart` objects to a PDF](#28-adding-chart-objects-to-a-pdf)  
    2.9 [Adding `Emoji` to a PDF](#29-adding-emoji-to-a-pdf)  
    2.10 [Container `LayoutElement` objects](#210-container-layoutelement-objects)  
        2.10.1 [Lists](#2101-lists)  
            2.10.1.1 [Working with `OrderedList`](#21011-working-with-orderedlist)  
            2.10.1.2 [Working with `RomanNumeralOrderedList`](#21012-working-with-romannumeralorderedlist)  
            2.10.1.3 [Working with `UnorderedList`](#21013-working-with-unorderedlist)  
            2.10.1.4 [Nesting `List` objects](#21014-nesting-list-objects)  
        2.10.2 [Tables](#2102-tables)  
            2.10.2.1 [`FixedColumnWidthTable`](#21021-fixedcolumnwidthtable)  
            2.10.2.2 [`FlexibleColumnWidthTable`](#21022-flexiblecolumnwidthtable)  
            2.10.2.3 [Setting layout properties on individual cells of a `Table`](#21023-setting-layout-properties-on-individual-cells-of-a-table)  
            2.10.2.4 [Incomplete `Table`](#21024-incomplete-table)  
            2.10.2.5 [Setting `column_span` and `row_span`](#21025-setting-col_span-and-row_span)  
    2.11 [Forms](#211-forms)  
        2.11.1 [Acroforms vs XFA](#2111-acroforms-vs-xfa)  
        2.11.2 [The `FormField` object](#2112-the-formfield-object)  
        2.11.3 [Adding `FormField` objects to a PDF](#2113-adding-formfield-objects-to-a-pdf)  
            2.11.3.1 [Adding a `TextField` to a PDF](#21131-adding-a-textfield-to-a-pdf)  
            2.11.3.2 [Customizing a `TextField` object](#21132-customizing-a-textfield-object)  
            2.11.3.3 [Pre-filling a `TextField` object](#21133-pre-filling-a-textfield-object)  
            2.11.3.4 [Adding a `DropDownList` to a PDF](#21134-adding-a-dropdownlist-to-a-pdf)  
            2.11.3.5 [Adding a `CountryDropDownList` to a PDF](#21135-adding-a-countrydropdownlist-to-a-pdf)  
            2.11.3.6 [Adding a `CheckBox` to a PDF](#21136-adding-a-checkbox-to-a-pdf)  
            2.11.3.7 [Adding a `RadioButton` to a PDF](#21137-adding-a-radiobutton-to-a-pdf)  
        2.11.4 [Changing the value of a `FormField` in an existing PDF](#2114-changing-the-value-of-a-formfield-in-an-existing-pdf)  
        2.11.5 [Getting the value of a `FormField` in an existing PDF](#2115-getting-the-value-of-a-formfield-in-an-existing-pdf)  
        2.11.6 [Flattening a `FormField`](#2116-flattening-a-formfield)  
    2.12 [Conclusion](#212-conclusion)            

3. [Working with existing PDFs](#3-working-with-existing-pdfs)  
    3.1 [Extracting meta-information](#31-extracting-meta-information)  
        3.1.1 [Extracting the author from a PDF](#311-extracting-the-author-from-a-pdf)  
        3.1.2 [Extracting the producer from a PDF](#312-extracting-the-producer-from-a-pdf)  
        3.1.3 [Using XMP meta-information](#313-using-xmp-meta-information)  
    3.2 [Extracting text from a PDF](#32-extracting-text-from-a-pdf)      
    3.3 [Extracting text using regular expressions](#33-extracting-text-using-regular-expressions)  
    3.4 [Extracting text using its bounding box](#34-extracting-text-using-its-bounding-box)  
    3.5 [Combining regular expressions and bounding boxes](#35-combining-regular-expressions-and-bounding-boxes)  
    3.6 [Extracting keywords from a PDF]()  
        3.6.1 [Extracting keywords from a PDF using tf-idf]()    
        3.6.2 [Extracting keywords from a PDF using textrank]()  
    3.7 [Extracting color information](#37-extracting-color-information)  
    3.8 [Extracting font information](#38-extracting-font-information)  
    3.9 [Extracting images from a PDF](#39-extracting-images-from-a-pdf)  
        3.9.1 [Modifying images in an existing PDF](#391-modifying-images-in-an-existing-pdf)  
        3.9.2 [Subsampling images in an existing PDF](#392-subsampling-images-in-an-existing-pdf)  
    3.10 [Working with embedded files](#310-working-with-embedded-files)  
        3.10.1 [Embedding files in a PDF](#3101-embedding-files-in-a-pdf)  
        3.10.2 [Extracting embedded files from a PDF](#3102-extracting-embedded-files-from-a-pdf)  
    3.11 [Adding annotations to a PDF](#311-adding-annotations-to-a-pdf)  
        3.11.1 [Adding geometric shapes](#3111-adding-geometric-shapes)  
        3.11.2 [Adding text annotations](#3112-adding-text-annotations)  
        3.11.3 [Adding link annotations](#3113-adding-link-annotations)  
        3.11.4 [Adding rubber stamp annotations](#3114-adding-rubber-stamp-annotations)  
    3.12 [Adding redaction (annotations)](#312-adding-redaction-annotations)  
        3.12.1 [Adding redaction annotations](#3121-adding-redaction-annotations)  
        3.12.2 [Applying redaction annotations](#3122-applying-redaction-annotations)  
    3.13 [Merging PDF documents](#313-merging-pdf-documents)  
    3.14 [Removing pages from PDF documents](#314-removing-pages-from--pdf-documents)  
    3.15 [Rotating pages in PDF documents](#315-rotating-pages-in-pdf-documents)        
    3.16 [Conclusion](#316-conclusion)  

4. [Heuristics for PDF documents](#4-heuristics-for-pdf-documents)  
    4.1 [Extracting tables from a PDF](#41-extracting-tables-from-a-pdf)  
    4.2 [Performing OCR on a PDF](#42-performing-ocr-on-a-pdf)  
    4.3 [Exporting PDF as a PIL Image](#43-exporting-pdf-as-a-pil-image)  
    4.4 [Exporting PDF as an SVG Image](#44-exporting-pdf-as-an-svg-image)    
    4.5 [Exporting Markdown as PDF](#45-exporting-markdown-as-pdf)  
    4.6 [Exporting HTML as PDF](#46-exporting-html-as-pdf)  

5. [Deep dive](#5-deep-dive)  
    5.1 [About PDF](#51-about-pdf)  
    5.2 [The XREF table](#52-the-xref-table)    
    5.3 [`Page` content streams](#53-page-content-streams)  
    5.4 [Postscript syntax](#54-postscript-syntax)  
    5.5 [Creating a `Document` using low-level syntax](#55-creating-a-document-using-low-level-syntax)  
    5.6 [Fonts in PDF](#56-fonts-in-pdf)  
        5.6.1 [Simple fonts](#561-simple-fonts)  
        5.6.2 [Composite fonts](#562-composite-fonts)  
    5.7 [About structured versus unstructered document formats](#57-about-structured-vs-unstructured-document-formats)  
        5.7.1 [Text extraction using heuristics to bridge the gap](#571-text-extraction-using-heuristics-to-bridge-the-gap)  
        5.7.2 [paragraph extraction and disjoint set](#572-paragraph-extraction-and-disjoint-set)  
    5.8 [Hyphenation](#58-hyphenation)  
        5.8.1 [The hyphenation problem](#581-the-hyphenation-problem)  
        5.8.2 [A fast and scalable hyphenation algorithm](#582-a-fast-and-scalable-hyphenation-algorithm)  
        5.8.3 [Using hyphenation in `borb`](#583-using-hyphenation-in-borb)  

6. [Showcases](#6-showcases)  
    6.1 [Creating an invoice](#61-showcase-creating-an-invoice)  
    6.2 [Creating a Sudoku puzzle](#62-showcase-creating-a-sudoku-puzzle)  
    6.3 [Creating a nonogram puzzle](#63-showcase-creating-a-nonogram-puzzle)  
    6.4 [Creating a tents-and-trees puzzle](#64-showcase-creating-a-tents-and-trees-puzzle)  
    6.5 [Using multiple `PageLayout` instances on the same `Page`](#65-showcase-using-multiple-pagelayout-instances-on-the-same-page)  
    6.6 [Creating a poem with custom `PageLayout`](#66-showcase-creating-a-poem-with-custom-pagelayout)  
    6.7 [Automatically processing an invoice](#67-showcase-automatically-processing-an-invoice)  

7. [Appendix](#7-appendix)
        
<div style="page-break-before: always;"></div>

# 1. `borb` in action

![enter image description here](img/chapter_illustrations/borb_001.jpg)

<div style="page-break-before: always;"></div>

## 1.1 About this book

This book will take you on an exploratory journey through the PDF format, and the `borb` Python library. You'll learn, through examples, how to use `borb` to generate and manipulate PDFs, and extract information from them. The deep-dive chapters will help you gain a thorough understanding of various interesting algorithms, or pieces of the PDF specification. The showcase examples are typically aimed at working out a use-case from start to finish.

## 1.2 About the author

![enter image description here](img/chapter_illustrations/about_the_author.jpg)

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

This book consists of 5 major parts:

- Creating PDF documents from scratch
- Manipulating existing PDF documents
- Heuristics for PDF documents
- Deep dive(s)
- Showcase(s)

### 1.5.1 Creating PDF documents

In this section you'll learn how to create a PDF from scratch. You'll explore the various `LayoutElement` objects that `borb` has to offer (`Paragraph`,  `Image`, `Table`, etc). You'll play around with the options for all of them (alignment, fonts, colors, layout, etc) and you'll get a good grasp of the basics of how to add content to a PDF.

This section will start out easy, by creating an empty PDF document and examining the contents therein. From there you'll learn how to add text, how to format that text, and how set various properties like font and color.

Then you'll explore other layout primitives, such as images and shapes (and their various sub-classes, such as QR-codes).

Once you have a firm grasp of the primitives, you'll learn how to aggregate those in more complex layout elements such as lists and tables.

After having read this section you should be able to code up a small proof of concept for any workflow that requires you to generate a PDF document.

### 1.5.2 Manipulate existing PDF documents

In this section you'll explore the things you can do with an existing PDF document. 

You'll start with the basics; merging existing documents, extracting and removing pages, making copies. These basics are a great way to learn more about `borb` and the underlying PDF syntax.

Having mastered these common use-cases, you'll move on to annotations. These provide a way to add content to existing documents. It can be as easy as stamping a page with "APPROVED", to adding a pop-up text note with remarks explaining an invoice-line.

PDF is sometimes said to be "where data goes to die". This is because data extraction from PDF can be a tricky job. In this section you'll learn several ways in which you can (attempt to) do this. Everything from extracting the entire textual content, to matching regular expressions, extracting text at specific locations, or combinations thereof. You'll also see how to extract images, color, and font-information, as well as how to embed files, or retrieve embedded files from a PDF. 

You'll explore redaction (the automated removal of content), which (in relation to GDPR) has known a resurgence. Automated redaction makes it easier for you to ensure people's privacy is upheld.

Lastly, you'll also tackle some common questions;

- Can you change the color of this text?
- Can you change this image?
- Can you change the font of this heading?
- Etc

### 1.5.3 Heuristics for PDF documents

This section talks about some of the more interesting (and difficult) algorithms used when working with PDF.
PDF is pretty much a "one way" format, it doesn't really lend itself to easily extracting information, or being modified.

This section provides you with the knowledge of some of the cutting-edge powertools to make PDF work for you and your company.

You'll learn how to extract tabular data from a PDF, and you'll jump under the hood for some common document-conversion dilemma's:

- PDF to JPEG
- PDF to JSON
- Markdown to PDF
- HTML to PDF

You'll also learn how to apply OCR (optical character recognition) to an existing document, so that it can later be processed by `borb` as if it contained text all along.

### 1.5.4 Deep-dive

This section explores PDF syntax and some of the core concepts in the `borb` library. Although it isn't a must for the day-to-day usage of `borb`, this section will certainly help build your appreciation for some of the limitations of PDF (or even PDF libraries).

You'll learn how content is rendered to a page, how the various layout-algorithms in `borb` work, how hyphenation works, and how you can attempt to reconstitute structural information from postscript syntax.

In this section I want to focus on the beautiful algorithms and data-structures I met along the way while implementing `borb`.

### 1.5.5 Showcases

This section provides end-to-end examples for some of the more common document-generation or document-manipulating use-cases. You should read this section last, as its content assumes you have worked your way through the basics beforehand.

You'll see:

- How to generate a realistic invoice
- How to generate a Sudoku puzzle
- How to extract text from an existing invoice
- Etc

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

![enter image description here](img/signature_joris_schellekens.png)

<div style="page-break-before: always;"></div>

