# 5 Working with existing PDFs

For some use-cases, you won't be creating the PDF's yourself. Imagine setting up a pipeline that automatically processes PDF invoices. Or even processing order forms.

Most of these workflows can be boiled down to some simple steps that can be handled with `borb`.

In this section you'll learn the ins and outs of working with existing PDF's.

![enter image description here](img/chapter_illustration.png)

<div style="page-break-before: always;"></div>

## 5.1 Extracting meta-information

Suppose you have a PDF document. Did you know it contains meta-information? Try it. Next time you have a PDF open in Adobe, press CTRL+D to open the document properties. You'll find things like:

- Author
- Producer
- Creation date
- Modification date
- Software that created the document
- Etc

It can be very useful to be able to extract these. Processing an invoice for instance might be more accurate if we know "supplier A uses software B to create their invoices, and python script C works best for that" versus "supplier X uses software Y, which is best handled by script Z".

### 5.1.1 Extracting the author from a PDF

In the next example you'll start by extracting the author from the PDF. 
This is of course assuming this property was set by whatever software created the PDF.

In order to be able to test these examples and get the same result as the book, I am providing a snippet of code here that will generate a very simple PDF;

```python
#!src/snippet_001.py
```

The PDF doesn't really look all that special when you open it.

![enter image description here](img/snippet_001_001.png)

But, when you open the properties (the exact shortcut differs depending on which PDF viewer you're using of course), you'll see the meta-data:

![enter image description here](img/snippet_001_002.png)

Now, let's assume you're getting this PDF (perhaps via email, or some automated process) and you'd like to extract the author from it.

`borb` allows you to do that in just a few lines of code:

```python
#!src/snippet_002.py
```

This will print `Joris Schellekens` to the terminal (in the case of the demo-PDF created by the earlier example of course).

Keep in mind that this property (`/Author`) is not mandatory. 
So the code may simply return (and thus print) `None`. 
This is not a bug, it simply means the `/Author` property was not explicitly set.

### 5.1.2 Extracting the producer from a PDF

Similarly, you can extract other properties, like the producer. This is typically the name of the piece of software that created the PDF (or last modified the PDF).

This is important. The PDF specification is not always precise or clear-cut. 
Some PDF software might do things a little differently than others, thus causing potential incompatibility.

You can easily mitigate this by checking the producer property, and separating the problematic files.

```python
#!src/snippet_003.py
```

Of course, now that you know how to extract the author and the producer, 
you can check out the other methods of `DocumentInfo` and find out even more about any PDF that comes your way.

### 5.1.3 using XMP meta information

This is from `adobe.com`:

> Adobe’s Extensible Metadata Platform (XMP) is a file labeling technology that lets you embed metadata into files themselves during the content creation process. 
> With an XMP enabled application, your workgroup can capture meaningful information about a project (such as titles and descriptions, searchable keywords, and up-to-date author and copyright information) in a format that is easily understood by your team as well as by software applications, hardware devices, and even file formats. 
> Best of all, as team members modify files and assets, they can edit and update the metadata in real time during the workflow.>

This next example is similar to the earlier example involving `DocumentInfo`.
But in stead, we will use `XMPDocumentInfo`. This class offers even more methods to get information from a PDF `Document`.

Keep in mind that XMP is not a requirement for a PDF `Document` to be valid. 
So you may find these methods return `None` when you test them on a `Document` that does not have embedded XMP data.

```python
#!src/snippet_004.py
```

For the document I tested, this printed:

```commandline
xmp.id:54e5adca-494c-4c10-983a-daa03cdae65a
```

<div style="page-break-before: always;"></div>

## 5.2 Extracting text from a PDF

Being able to extract text from a PDF is a fundamental skill. 
In the deep-dive, you'll learn more about PDF syntax, and why text-extraction is a non-trivial thing.

For now, you can start with an easy example where all visible text on the page is extracted.

This extraction process does not take into account any structure that may be present on the page itself. 
Hence the name `SimpleTextExtraction`.

You'll be using the same input PDF as earlier (containing a paragraph of lorem ipsum).

```python
#!src/snippet_005.py
```

Here you've used the alternative method for `PDF.loads` which takes an array of `EventListener` objects as its argument.

`PDF.loads` will open the PDF, and start processing PDF syntax. 
Whenever it handles certain commands (rendering text, rendering images, switching to a new page, etc), 
it will send out `Event` objects. These can be handled by the appropriate `EventListener` implementation.

`SimpleTextExtraction` is one of those `EventListener` implementations that listens to:

- The start of a `Page`
- The end of a `Page`
- Begin rendering text mode
- Stop rendering text mode
- Render text command(s)

The code above should print out:

```
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation
ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in
reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint
occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est
laborum.
```

<div style="page-break-before: always;"></div>

## 5.3 Extracting text using regular expressions

This is a much more advanced way to extract text from a PDF. 
By using regular expressions, you can easily look for things like "total amount due" followed by some numbers. 
And, in doing so, effectively retrieve the useful data from an invoice.

In the next example you'll be doing exactly that. 
The code is very similar to what you've done earlier.

```python
#!src/snippet_006.py
```

Like before, you constructed an implementation of `EventListener` and passed it to the `PDF.loads` method. 
`RegularExpressionTextExtraction` takes a regular expression as its single argument.

Once the `Document` has been parsed, you can retrieve all matches by specifying a `page_nr`. 
Pages are numbered from 0.

You'll get back a `typing.List[PDFMatch]` which is meant to behave like a `re.Match` object. 
Most of its fields and methods are written to work interchangeably with `re.Match`.

Of course, because a PDF has a dimensionality to it (content is located on an x/y plane), 
there are some extra methods. Such as `get_bounding_boxes()` which returns a `typing.List[Rectangle]'.

You may be wondering why a single match against a regular expression would return multiple bounding boxes. 
This happens when content is matched over multiple lines.

In this example however, the output should be:

```
0 Lorem ipsum dolor
	59.500000 740.916000 99.360000 11.100000
```

indicating a single match, with text "lorem ipsum dolor", 
with bounding box (lower left corner) at `[59.5, 740.916]` and a width of `99.36` and a height of `11.1`.

<div style="page-break-before: always;"></div>

## 5.4 Extracting text using its bounding box

Another extraction process relies on the rendering of the PDF itself. 
Perhaps the PDF's you are processing always have some kind of information at a precise location 
(e.g. an invoice number in the top right corner).

This implementation of `EventListener` allows you to filter events (i.e. rendering instructions) by providing `borb` with a bounding box.

In the next example you'll be using the coordinates from the previous example, to build a filter for `SimpleTextExtraction`.

```python
#!src/snippet_007.py
```

This prints:

```commandline
Lorem ipsum dolor
```

<div style="page-break-before: always;"></div>

## 5.5 Combining regular expressions and bounding boxes

Of course, `borb` is designed to be a library, 
so the idea of being able to strap together your own tools using the toolkit is very important to me.

In the next example you'll be combining a regular expression expression extraction technique with a bounding box.

First you'll be looking for the precise location of the text "nisi ut aliquip". 
Once you have matched this regular expression, you also have its location on the page.

Then you can extend this box, 
knowing the text you'd really like to extract will be on the right of that piece of text.

```python
#!src/snippet_008.py
```

This example is a lot to take in. 
Try it out, read through it carefully. 
It's important to understand these basic concepts in `borb` to really get the most out of it.

This example starts out similar to the earlier example ["Extracting text using regular expressions"](#33-extracting-text-using-regular-expressions), 
it uses the returned `PDFMatch` to determine the location of the text. 
With this location it processes the `Document` again, filtering a modified bounding box.

This example prints:

```commandline
ex ea commodo conse uat. Duis aute irure dolor in
```

This example might seem contrived, but there are definitely use-cases where this exact behavior comes in handy. 
Imagine processing a `Document`, looking for "amount due", 
and then modifying the bounding box to retrieve the amount and currency that is typically next to it.

The same strategy can be used to extract addresses from invoices, or anything similar really.

<div style="page-break-before: always;"></div>

## 5.6 Extracting keywords from a PDF

### 5.6.1 Extracting keywords from a PDF using TF-IDF

From wikipedia:

> In information retrieval, tf–idf, TF*IDF, or TFIDF, short for term frequency–inverse document frequency, is a numerical statistic that is intended to reflect how important a word is to a document in a collection or corpus. 
> It is often used as a weighting factor in searches of information retrieval, text mining, and user modeling. 
> The tf–idf value increases proportionally to the number of times a word appears in the document and is offset by the number of documents in the corpus that contain the word, which helps to adjust for the fact that some words appear more frequently in general. 
> tf–idf is one of the most popular term-weighting schemes today.

#### 5.6.1.1 Term Frequency

From wikipedia:

> Suppose we have a set of English text documents and wish to rank them by which document is more relevant to the query, "the brown cow". 
> A simple way to start out is by eliminating documents that do not contain all three words "the", "brown", and "cow", but this still leaves many documents. 
> To further distinguish them, we might count the number of times each term occurs in each document; the number of times a term occurs in a document is called its term frequency. 
> However, in the case where the length of documents varies greatly, adjustments are often made (see definition below). 

#### 5.6.1.2 Inverse document frequency

From wikipedia:

> Because the term "the" is so common, term frequency will tend to incorrectly emphasize documents which happen to use the word "the" more frequently, without giving enough weight to the more meaningful terms "brown" and "cow". 
> The term "the" is not a good keyword to distinguish relevant and non-relevant documents and terms, unlike the less-common words "brown" and "cow". Hence, an inverse document frequency factor is incorporated which diminishes the weight of terms that occur very frequently in the document set and increases the weight of terms that occur rarely.

#### 5.6.1.3 Using TF-IDF in `borb`

Let's start by creating a `Document` with a few `Paragraph` objects in it.
Since you'll be eliminating stop words (which are language-dependent), this `Document` needs to contain sensible English text.
You'll be creating a `Document` containing information about "Lorem Ipsum".

```python
#!src/snippet_009.py
```

This should produce a `Document` like this:

Now you can unleash `TFIDFKeywordExtraction` on the `Document` you made;

```python
#!src/snippet_010.py
```

This outputs:

```commandline
/usr/bin/python3.8 /home/joris/Code/borb-examples-dev/chapter_005/src/snippet_010.py
[('LOREM', 9.100909090909093e-06), 
 ('IPSUM', 9.100909090909093e-06), 
 ('TEXT', 2.737272727272727e-06), 
 ('LATIN', 2.737272727272727e-06)]

Process finished with exit code 0
```

### 5.6.2 Extracting keywords from a PDF using  textrank

TextRank is a graph-based ranking model for text processing which can be used in order to find the most relevant sentences in text and also to find keywords. 
The algorithm is explained in detail in the paper at https://web.eecs.umich.edu/~mihalcea/papers/mihalcea.emnlp04.pdf

```python
#!src/snippet_011.py
```

This outputs:

```commandline
/usr/bin/python3.8 /home/joris/Code/borb-examples-dev/chapter_005/src/snippet_011.py
[('LOREM', 9.100909090909093e-06), 
 ('IPSUM', 9.100909090909093e-06), 
 ('TEXT', 2.737272727272727e-06), 
 ('LATIN', 2.737272727272727e-06)]

Process finished with exit code 0
```

<div style="page-break-before: always;"></div>

## 5.7 Extracting color-information

This is perhaps a bit more of a tangent, but I can imagine it may be useful. 
In this particular example you'll be extracting color-information from a PDF.

Given the previous examples, you can easily adapt this technique to build a filter (similar to the location-based filter). 

By doing so, you unlock the possibility of processing a PDF by saying "look for text in the color red" or "look for text in the top right corner, in blue".

In this example, you'll be using `ColorSpectrumExtraction` to retrieve all the colors on the `Page`. This is a stepping stone to building bigger and better things. Although in and of itself this can already be useful to determine color-blindness compatibility of a given `Document`.

In the deep-dive, you'll learn the ins and outs of implementing your own `EventListener`.

To start this example, you'll be creating a PDF containing multiple colors. You'll be adding 3 `Paragraph` objects (red, green, blue) and one `Image`.

```python
#!src/snippet_012.py
```

![enter image description here](img/snippet_012.png)

This `Document` will serve as the input for the extraction example. 

Rather than printing the result of the extraction to the command-line, 
you'll create an output-pdf. I think it's a lot more visual to actually see the colors that were extracted, 
rather than having their RGB values printed out on the console.

```python
#!src/snippet_013.py
```

![enter image description here](img/snippet_013.png)

<div style="page-break-before: always;"></div>

## 5.8 Extracting font-information

In this example you'll be extracting font-names from an existing PDF.
This may be useful (in later examples) to handle situations in which you know a certain snippet of information is always written in a particular font.

You'll start by creating a PDF with several fonts;

```python
#!src/snippet_014.py
```

![enter image description here](img/snippet_014.png)

And now you can process that PDF and retrieve the fonts;

```python
#!src/snippet_015.py
```

This prints:

```commandline
['Helvetica', 'Helvetica-Bold', 'Courier']
```

You can of course go looking at the code for `FontExtraction` (I highly encourage you to do so).
This should enable you to write your own filter (similar to `LocationFilter`) to filter on fonts.

### 5.8.1 Filtering by `font`

In this example you'll be using `FontNameFilter` to retrieve all text on a `Page` that was written in `Courier`.
First things first though, let's create an example PDF with text in different fonts;

```python
#!src/snippet_016.py
```

This generates the following PDF:

![enter image description here](img/snippet_016.png)

Now we can run the code to filter on `font_name`:

```python
#!src/snippet_017.py
```

This should print:

```commandline
Hello World, from Courier!
```

### 5.8.2 Filtering by `font_color`

Being able to filter by `font_color` allows you to extract text in a much more fine-grained way.
You could filter out only the red text from an invoice, 
or combine this particular filter with other filter implementations and do even crazier things.

This implementation of `EventListener` takes 2 arguments at construction:

- `color` : The `Color` you'd like to keep
- `maximum_normalized_rgb_distance` :   This is the maximum allowable distance between the `Color` in the PDF and the `color` parameter. This allows you to filter on "everything that looks kinda red" rather than "everything that is this exact shade of red".                                  
                                        The distance is defined as ((r0 - r1)² - (g0 - g1)² + (b0 - b1)²) / 3, with r, g, b being the red, green, blue components of the `Color`.

We're going to start by creating an input PDF with text in various colors.

```python
#!src/snippet_018.py
```

This generates the following PDF:

![enter image description here](img/snippet_018.png)

Now we can filter the text in the PDF by selecting the red letters:

```python
#!src/snippet_019.py
```

This should print:

```commandline
Hello World, in Red!
```

<div style="page-break-before: always;"></div>

## 5.9 Extracting images from a PDF

In this example you'll be extracting images from an existing PDF.
Keep in mind the images may be subject to copyright, they may not have been intended for you to be able to extract them.

To get started, let's briefly re-iterate one of the earlier examples about inserting an `Image` object in a PDF.

```python
#!src/snippet_020.py
```

![enter image description here](img/snippet_020.png)

Now that you have an input `Document`, let's go ahead and extract the `Image` from it.

```python
#!src/snippet_021.py
```

This should print:

```
<PIL.JpegImagePlugin.JpegImageFile image mode=RGB size=2000x3000 at 0x7F3BE45E5C40>
<PIL.JpegImagePlugin.JpegImageFile image mode=RGB size=4000x6000 at 0x7F3BE43FB760>
<PIL.JpegImagePlugin.JpegImageFile image mode=RGB size=2640x3300 at 0x7F3BE441B580>
```

What's interesting is that even though you inserted the `Image` objects and specified a particular size, the extracted `Image` is actually a lot larger. 
This is because PDF simply has its own way of dealing with resizing images. 
And there are use-cases where you might actually want this behavior. 

You could embed a tiny example of an `Image` in a `Document`, 
knowing the recipient can extract the full (much richer) `Image`.

Of course, if you're using this `Image` as a company logo, 
or part of the header/footer of the `Document`, 
you typically want the image to be as small as possible (while remaining legible).

In one of the upcoming examples you'll see how to subsample an `Image` in a PDF, 
and you'll see firsthand how this technique can help reduce your document's memory footprint.

### 5.9.1 Modifying images in an existing PDF

In this example you'll be modifying the images in a PDF.
You'll be using the PDF you created earlier (with 3 pineapple images) as a starting point.

First you'll be exploring the PDF, using the JSON-like structure `borb` has created.

```python
#!src/snippet_022.py
```

This code prints:

```
Im1	<PIL.JpegImagePlugin.JpegImageFile image mode=RGB size=2000x3000 at 0x7F74380D0490>
Im2	<PIL.JpegImagePlugin.JpegImageFile image mode=RGB size=4000x6000 at 0x7F7437F1B970>
Im3	<PIL.JpegImagePlugin.JpegImageFile image mode=RGB size=2640x3300 at 0x7F74367D56D0>
```

This example shows us that the PDF has stored the `Image` objects in the `Page` under `Resources\XObject\Im1` (and `Im2`, `Im3` respectively).

You can now modify these and store the `Document`.

First, you'll write this simple function to convert an `Image` to its sepia counterpart.
"sepia" is just a fancy way of saying "old timey brown pictures".

```python
#!src/snippet_023.py
```

The result should look like this:

![enter image description here](img/snippet_023.png)

### 5.9.2 Subsampling images in an existing PDF

As you've found out in a previous example, sometimes the dimensions at which an `Image` is displayed are not the same as the dimensions at which it was stored.
This can lead to a rather bulky PDF, if each `Image` is substantially larger than its display-dimensions.

In the next example, you'll be fixing that. 
Luckily `borb` comes with `ImageFormatOptimization` which does all the heavy lifting for you.

As a benchmark, you can first have a look at the file-characteristics of the original input PDF.

![enter image description here](img/snippet_024_001.png)

You can see the file is roughly 5Mb large.
Now you can use the following code to optimize the `Image` dimensions:

```python
#!src/snippet_024.py
```

When you check out the file-stats on the output-file, the difference is astonishing:

![enter image description here](img/snippet_024_002.png)

You'll see that the output file looks the same, although there may have been some quality loss in the images.

![enter image description here](img/snippet_024_003.png)

<div style="page-break-before: always;"></div>

## 5.10 Working with embedded files

PDF is more than just a digital paper-replacement. 
PDF also has some features that go beyond "imitating paper".
For instance PDF allows you embed one or multiple files inside the document. 
By doing so, you can provide extra resources for whoever reads the document.

In one particular use-case, a german invoicing standard (ZUGFeRD) requires the creator of the invoice to embed an XML representation of the invoice, 
to ensure the document can be processed automatically.

In this section you'll handle both extraction of embedded files, and appending embedded files to a `Document`.

### 5.10.1 Embedding files in a PDF

In this example, you'll be creating a `Document` containing one `Paragraph`, and embed a json-file.

```python
#!src/snippet_025.py
```

The PDF should look something like this: 

![enter image description here](img/snippet_025_001.png)

Notice the warning you see atop the PDF viewer. 
This may of course vary depending on the viewer you're using.
If you open the embedded file pane (again depending on your editor) you may see something similar to this:

![enter image description here](img/snippet_025_002.png)

### 5.10.2 Extracting embedded files from a PDF

Now that you can embed files in a PDF, let's see how you can retrieve those files again.

```python
#!src/snippet_026.py
```

This should print:

```
lorem_ipsum.json, 66 bytes
```

Of course, rather than just displaying the byte-count you could also write the bytes to a file again.
Or process them directly using the `io` API in Python.

<div style="page-break-before: always;"></div>

## 5.11 Merging PDF documents

This is one of the most common usecases in working with PDF.
In the next example you'll be merging multiple existing PDF documents.

You'll start by creating two methods that each create (and write) a PDF document.

```python
#!src/snippet_027.py
```

![enter image description here](img/snippet_027.png)

That should take care of the first PDF.
Now you can write a second (similar) PDF document:

```python
#!src/snippet_028.py
```

![enter image description here](img/snippet_028.png)

Finally, you can write the main method, which will create both documents, read them, and merge them.

```python
#!src/snippet_029.py
```

![enter image description here](img/snippet_029.png)

You don't have to fully merge both `Document` objects, you can just copy a couple of `Page` objects from one `Document` to another.     
In the next example you'll be selecting one `Page` from each `Document` and building a new PDF with them.

You'll start by creating a slightly modified version of the first document from the previous example.
This document has 10 pages.

```python
#!src/snippet_030.py
```

The page number is printed atop each page, to make it easier to identify them later.

![enter image description here](img/snippet_030.png)

The second document will also have 10 pages. The page number will also be displayed atop each page:

```python
#!src/snippet_031.py
```

![enter image description here](img/snippet_031.png)

To build the merged document you'll be selecting a page from each input document in turn, until the merged document has 10 pages.

```python
#!src/snippet_032.py
```

The final document alternates pages between both input documents (which is obvious from the color and page numbers).

![enter image description here](img/snippet_032.png)

<div style="page-break-before: always;"></div>

## 5.12 Removing pages from  PDF documents

Sometimes you may want to remove a `Page` from a PDF.
e.g. removing a cover-page before text-extraction may speed things up (one less page to process)

In the next example you'll be removing the first `Page` from a `Document`.
First of course, we need to create a `Document` to start with;

```python
#!src/snippet_033.py
```

![enter image description here](img/snippet_033.png)

Now that we have a substantial `Document`, we can remove a `Page` from it;

```python
#!src/snippet_034.py
```

![enter image description here](img/snippet_034.png)

You can see (in the thumbnail panel on the left side) that the second page was removed.

<div style="page-break-before: always;"></div>

## 5.13 Rotating pages in PDF documents

In this example you'll be rotating a `Page` 90 degrees clockwise. 
You can rotate a `Page` any multiple of 90 degrees.

```python
#!src/snippet_035.py
```

![enter image description here](img/snippet_035.png)

You already know this PDF, it's the same from the previous examples.

Now let's rotate a `Page`:

```python
#!src/snippet_036.py
```

![enter image description here](img/snippet_036.png)

<div style="page-break-before: always;"></div>

## 5.14 Conclusion

In this section you've learned the basics of working with existing PDF documents. 
You've seen how to extract text, regular expressions, images, font-information and color-information.

And you've seen the basics of merging PDF's and removing one or more pages from a PDF.

This section, together with the previous wraps up the basics of what you can do with `borb`.

I would encourage you to continue reading, and more importantly to continue exploring `borb`.
There are many more options and algorithms that you may find useful. 
As a developer, expanding your toolkit with more knowledge is never a bad thing.

<div style="page-break-before: always;"></div>
