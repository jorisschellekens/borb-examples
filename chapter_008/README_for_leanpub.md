# 8 Deep Dive into `borb`

![enter image description here](https://raw.githubusercontent.com/jorisschellekens/borb-examples/master/chapter_008/img/chapter_illustration.jpg)

{pagebreak}

## 8.1 About PDF

If we consider PDF as a programming language, then these would be its primitive data-types:

- Strings (either as plaintext, or hexadecimal)
- Numbers
- Booleans
- Name objects (think of these as "reserved strings")

From which the bigger objects are built:

- Dictionaries (maps name objects to any value, delimited by `<<` and `>>`)
- Arrays (delimited by `[` and `]`)
- Streams (these typically represent binary compressed data)
- References

This is an example dictionary object:

```
<<  /Root 1 0 R 
    /Info 2 0 R 
    /Size 18 
    /ID [<02c1677f2c452985480d6a68b2cdfe96> <02c1677f2c452985480d6a68b2cdfe96>]
    >>
```

The keys are name objects:

- `/Root`
- `/Info`
- `Size`
- `ID`

Objects such as `1 0 R` are references. They need to be resolved by the XREF (more on that later).

```
[<02c1677f2c452985480d6a68b2cdfe96> <02c1677f2c452985480d6a68b2cdfe96>]
```

is an array containing two hexadecimal string objects.

## 8.2 The XREF table

The cross-reference table in a PDF is one of many tricks designed to speed up a reader. A cross-reference table (further abbreviated as XREF) contains a mapping of all PDF objects and their byte offset.

A conforming reader will start reading a PDF backwards, reading the `startxref` keyword. 

This is an example XREF:

```
xref
0 18
0000000000 00000 f
0000000015 00000 n
0000381959 00000 n
0000000064 00000 n
0000381716 00000 n
0000000121 00000 n
0000000273 00000 n
0000052510 00000 n
0000052542 00000 n
0000052583 00000 n
0000381619 00000 n
0000052752 00000 n
0000055981 00000 n
0000371339 00000 n
0000056194 00000 n
0000371411 00000 n
0000381788 00000 n
0000381888 00000 n
trailer
<</Root 1 0 R /Info 2 0 R /Size 18 /ID [<02c1677f2c452985480d6a68b2cdfe96> <02c1677f2c452985480d6a68b2cdfe96>]>>
startxref
382063
%%EOF
```

Just after the `startxref` keyword you'll find a number representing the byte offset at which the start of the XREF can be found.

The start of the XREF table is delimited with the `xref` keyword. 
Just after it you'll find two numbers (`0 18`). This means the first object of the PDF starts at number 0, and this XREF table contains 18 objects. 

Each is responsible for a line like:

```
0000000273 00000 n
```

This is the 7th line of the XREF, so this line relates to object number 7. It says object 7 can be found at byte offset `0000000273`.
The second number on that line represents the `generation`. 
PDF allows you to revise a document. 
So each object has a generation to signify whether it belongs to a particular revision of the PDF.

The last part of each line is `n` or `f`. `n` means the object is currently is use. Objects marked with `f` should be considered as non-content.

The XREF also contains the trailer dictionary. This dictionary is the starting point of the PDF object tree.

```
<</Root 1 0 R /Info 2 0 R /Size 18 /ID [<02c1677f2c452985480d6a68b2cdfe96> <02c1677f2c452985480d6a68b2cdfe96>]>>
```

- `/Root` is where the actual content objects of the PDF begin. In this trailer, the `/Root` entry points to object `1 (generation 0)`.
- `/Info` points to the info-dictionary, which is where you'll find the meta-data such as author, producer, modification date, etc. In this trailer, the `/Info` entry points to object `2 (generation 0)`.

If you follow the `/Root` entry, you'll find something like:

```
1 0 obj
<</Type /Catalog /Pages 3 0 R /Outlines 4 0 R>>
endobj
``` 

The `/Pages` entry points to an array (one element per page), which form the beginning of the page-content.

```
3 0 obj
<</Count 1 /Kids [5 0 R] /Type /Pages>>
endobj
```

Each entry in the `/Kids` array represents a single `Page`.

```
5 0 obj
<</Type /Page /MediaBox [0 0 595 842] /Parent 3 0 R /Contents 6 0 R /Resources 7 0 R>>
endobj
```

`/Contents` points to the `Page` content stream. This is a string of postfix instructions (usually compressed using `deflate`).

### 8.2.2 Dealing with a broken XREF
 
A PDF document is considered *broken* if it no longer opens:
- in Adobe Reader (or a similar PDF reader)
- in `borb`

The reason why those two are different criteria is that Adobe is very lenient when it comes to enforcing the PDF standards. Which is understandable, you want PDF reading software to be able to read as many documents as possible.

`borb` however tends to be very strict when it comes to dealing with PDF documents (in fact most PDF generators are).

When a PDF no longer opens, it is usually down to the `XREF` being incorrect. Which is to say, some byte-miscount in the document.
Remember, the PDF document is supposed to announce at which byte the `XREF` table begins. If that byte-count is off by even 1 byte, the `XREF` table is (from the standpoint of the PDF spec) no longer in the right location.

To fix this, `borb` has a last-resort parser to rebuild an `XREF`, this is the `RebuiltXREF` class.
This parser will go over the entire PDF, looking for object declarations, and keep track of their byte count. This is effectively reverse-engineering the `XREF` document (at the cost of having to run over the entire file).

Whenever `borb` is forced to do this, you may expect the logging to indicate as such.

## 8.3 Page content streams

In the previous section you explored the top-level objects of a PDF.
You got all the way down to the `Page` object.
Now you can look under the hood and see the instructions in the content stream.

```
6 0 obj
<</Length 52185>>
stream

            q
            BT
            0.521569 0.780392 0.870588 rg
            /F1 1.000000 Tf
            24.000000 0 0 24.000000 59.500000 725.760000 Tm
            (Hello World!) Tj
            ET
            Q 

            q
            ... etc ...
```

This is the (inflated) page content stream. It contains the raw instructions for rendering content on the `Page`.
Operators are prefix operators, meaning the arguments come before the operator.

- `q` : pushes a new graphics environment on the stack
- `BT` : begin text
- `0.521569 0.780392 0.870588 rg` : set the color (using RGB color mode)
- `/F1 1.000000 Tf` : use the font specified in `/Resources/Font/F1`, at size `1`
- `24.000000 0 0 24.000000 59.500000 725.760000 Tm` : sets the font-transformation matrix (essentially setting the font size to 24, and setting the text position)
- `(Hello World!) Tj` : render the text "Hello World!"
- `ET` : end text
- `Q` : pop the last element from the graphics environment stack

{pagebreak}

## 8.4 Postscript syntax

This section provides you with a quick overview of the most common PDF operators.
This is meant to enable you to debug PDF documents.

For a more detailed explanation I would advise you to check out the PDF-specification.
A free copy of which can be found:

- In the `borb` GitHub repository
- On the Adobe website

| Operator | Number of arguments | Type of arguments | Description                                                                                                                                                                                                                                                                                                                                                                                                   |
|----------|---------------------|-------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| b | 0                   |                   | Close, fill, and stroke path using nonzero winding number rule                                                                                                                                                                                                                                                                                                                                                |
| B | 0                   |                   | Fill and then stroke the path, using the nonzero winding number rule to determine the region to fill.                                                                                                                                                                                                                                                                                                         |
| b* | 0                   |                   | Close, fill, and then stroke the path, using the even-odd rule to determine the region to fill.                                                                                                                                                                                                                                                                                                               |
| B* | 0                   |                   | Fill and then stroke the path, using the even-odd rule to determine the region to fill.                                                                                                                                                                                                                                                                                                                       |
| BDC | 2                   |                   | Begin a marked-content sequence with an associated property list, terminated by a balancing EMC operator. tag shall be a name object indicating the role or significance of the sequence. properties shall be either an inline dictionary containing the property list or a name object associated with it in the Properties subdictionary of the current resource dictionary (see 14.6.2, “Property Lists”). |
| BI | 0                   |                   | Begin an inline image object.                                                                                                                                                                                                                                                                                                                                                                                 |
| BMC | 1                   |                   | Begin a marked-content sequence terminated by a balancing **EMC** operator. tag shall be a name object indicating the role or significance of the sequence.                                                                                                                                                                                                                                                   |
| BT |
| BX |
| c |
| cm |
| CS |
| cs |
| d |
| d0 |
| d1 |
| Do |
| DP | 2                   |                   | Designate a marked-content point with an associated property list. tag shall be a name object indicating the role or significance of the point. properties shall be either an inline dictionary containing the property list or a name object associated with it in the Properties subdictionary of the current resource dictionary (see 14.6.2, “Property Lists”).                                           |
| EI | 0                   |                   | End an inline image object.                                                                                                                                                                                                                                                                                                                                                                                   |
| EMC | 0                   |                   | End a marked-content sequence begun by a **BMC** or **BDC** operator.                                                                                                                                                                                                                                                                                                                                         |
| ET |
| EX |
| f | 0                   |                   | Fill the path, using the nonzero winding number rule to determine the region to fill (see 8.5.3.3.2, "Nonzero Winding Number Rule"). Any subpaths that are open shall be implicitly closed before being filled.                                                                                                                                                                                               |
| F | 0                   |                   | Equivalent to **f**; included only for compatibility. Although PDF reader applications shall be able to accept this operator, PDF writer applications should use **f** instead.                                                                                                                                                                                                                               |
| f* | 0                   |                   | Fill the path, using the even-odd rule to determine the region to fill (see 8.5.3.3.3, "Even-Odd Rule").                                                                                                                                                                                                                                                                                                      |
| G |
| g |
| gs |
| h |
| i |
| ID | 0                   |                   | Begin the image data for an inline image object.                                                                                                                                                                                                                                                                                                                                                              |
| j |
| J |
| K |
| k |
| l | 2                   |                   | Append a straight line segment from the current point to the point (x, y). The new current point shall be (x, y).                                                                                                                                                                                                                                                                                             |
| m | 2                   |                   | Begin a new subpath by moving the current point to coordinates (x, y), omitting any connecting line segment. If the previous path construction operator in the current path was also m, the new m overrides it; no vestige of the previous m operation remains in the path.                                                                                                                                   |
| M |
| MP | 1                   |                   | Designate a marked-content point. tag shall be a name object indicating the role or significance of the point.                                                                                                                                                                                                                                                                                                |
| n | 0                   |                   | End the path object without filling or stroking it. This operator shall be a path-painting no-op, used primarily for the side effect of changing the current clipping path (see 8.5.4, "Clipping Path Operators").                                                                                                                                                                                            |
| q |
| Q |
| re |
| RG |
| rg |
| ri |
| s | 0                   |                   | Close and stroke the path.                                                                                                                                                                                                                                                                                                                                                                                    |
| S | 0                   |                   | Stroke the path.                                                                                                                                                                                                                                                                                                                                                                                              |
| SC |
| sc |
| SCN |
| scn |
| sh |
| T* |
| Tc |
| Td |
| TD |
| Tf |
| Tj |
| TJ |
| TL |
| Tm |
| Tr |
| Ts |
| Tw |
| Tz |
| v |
| w |
| W |
| W* |
| y |
| ' |
| " |

{pagebreak}

## 8.5 Creating a `Document` using low-level syntax

In this subsection I'll take you through all of the relevant pieces of `borb` when rendering a small piece of text to a PDF.
This is a bit like having someone sit next to you, explaining the code while you're stepping through it with a debugger.
I hope this subsection teaches you some of the internal workings of `borb` and helps you gain a better understanding of where to look should you encounter any problems.

Now that you have some knowledge of the low-level syntax of PDF, you can try to build a PDF document.
In this example, you're going to create a PDF with the text "Hello World!".
This time, you'll be using only the low-level syntax. Later, you'll see how the `LayoutElement` objects end up writing this content to the PDF.

Although this is not very practical it will do several things:

- Give you a deeper appreciation for PDF libraries
- Grant you to power to specify the document exactly as you want, now that you understand PDF at its finest
- Enable you to write your own `LayoutElement` implementations (if needed) 

In this example, you'll be creating a PDF from scratch, containing "Hello World!", using only the low-level syntax.

{pagebreak}

## 8.6 Fonts in PDF

A font shall be represented in PDF as a dictionary specifying the type of font, its PostScript name, its encoding,
and information that can be used to provide a substitute when the font program is not available. Optionally, the
font program may be embedded as a stream object in the PDF file.

### 8.6.1 Simple fonts

There are several types of simple fonts, all of which have these properties:
- Glyphs in the font shall be selected by single-byte character codes obtained from a string that is shown by
the text-showing operators. Logically, these codes index into a table of 256 glyphs; the mapping from
codes to glyphs is called the font’s encoding. Under some circumstances, the encoding may be altered by
means described in 9.6.6, "Character Encoding".
- Each glyph shall have a single set of metrics, including a horizontal displacement or width, as described in
9.2.4, "Glyph Positioning and Metrics"; that is, simple fonts support only horizontal writing mode.
- Except for Type 0 fonts, Type 3 fonts in non-Tagged PDF documents, and certain standard Type 1 fonts,
every font dictionary shall contain a subsidiary dictionary, the font descriptor, containing font-wide metrics
and other attributes of the font; see 9.8, "Font Descriptors". Among those attributes is an optional font file
stream containing the font program.

### 8.6.2 Composite fonts

A composite font, also called a Type 0 font, is one whose glyphs are obtained from a fontlike object called a
CIDFont. A composite font shall be represented by a font dictionary whose Subtype value is Type0. The Type
0 font is known as the root font, and its associated CIDFont is called its descendant.

**NOTE 1:**
Composite fonts in PDF are analogous to composite fonts in PostScript but with some limitations. In particular,
PDF requires that the character encoding be defined by a CMap, which is only one of several encoding
methods available in PostScript. Also, PostScript allows a Type 0 font to have multiple descendants, which
might also be Type 0 fonts. PDF supports only a single descendant, which shall be a CIDFont.

When the current font is composite, the text-showing operators shall behave differently than with simple fonts.
For simple fonts, each byte of a string to be shown selects one glyph, whereas for composite fonts, a sequence
of one or more bytes are decoded to select a glyph from the descendant CIDFont.

**NOTE 2:**
This facility supports the use of very large character sets, such as those for the Chinese, Japanese, and
Korean languages. It also simplifies the organization of fonts that have complex encoding requirements.

{pagebreak}

## 8.7 About structured vs. unstructured document formats

Typically, at one point or another when you're working with PDF, someone will come along that would like to convert the PDF to some other format.
Most libraries or software-tools offer all kinds of wacky conversions. Some more successful than others.
The reason for the varying degrees of success is not just to do with the diligence of the creator, but rather the chasm between structured and unstructured document formats;

- structured document format: every piece of content is typically provided with
    - coordinates (or coordinates can be derived using a layout algorithm)
    - a logical structure
  In `HTML` for instance, a `<p>` element is rendered on a browser (it has coordinates), and all the text inside that element knows it is part of that paragraph. The paragraph itself may be part of some other element (a `<table>` or `<li>`, etc).
- unstructured document format: no logical structure (or no such structure is mandatory)

PDF is an unstructured format.   
You've explored the rendering instructions that make up a `Page`, and you will have noticed there is no indicator to say "all these instructions belong to one paragraph", or "this paragraph belongs to a table".
You can of course do this (the PDF standard provides so called "tagged" PDF), but is rare to see such PDFs in the wild.

So, when extracting text from a PDF `borb` is faced with several issues:

- text rendering instructions do not make it clear where a paragraph begins/ends
- the `space` character can either be encoded in the rendering instructions, but it can also be omitted (you can simply move the drawing cursor a few dots to the right)
- text rendering instructions do not need to appear in any particular order

In order to be able to extract text, `borb` has to do a lot of work. Let's have a look behind the scenes to see what goes on.

### 8.7.1 Text extraction: using heuristics to bridge the gap

In `borb`, the easiest way of accessing the text on a page is by using `SimpleTextExtraction`.
Let's have a look at how it works.

First, there is `ChunkOfTextRenderEvent`:

```python
class ChunkOfTextRenderEvent(Event, ChunkOfText):
    """
    This implementation of Event is triggered right after the Canvas has processed a text-rendering instruction
    """

    def __init__(self, graphics_state: CanvasGraphicsState, raw_bytes: String):
        ... etc ...
```

This class represents the call-back information that is passed to `EventListener` objects.
Whenever `borb` processes the page content-stream, every operator has the opportunity to send out these `Event` objects to `EventListener` implementations.     

This is the `ShowText` operator (the `Tj` operator in postscript);

```python
class ShowText(CanvasOperator):
    """
    Show a text string.
    """

    def __init__(self):
        super().__init__("Tj", 1)

    def invoke(self, canvas_stream_processor: "CanvasStreamProcessor", operands: List[AnyPDFType] = []) -> None:  # type: ignore [name-defined]
        """
        Invoke the Tj operator
        """
        ... etc ...

```

In its `invoke` method, you'll find the call that sends out one of these `ChunkOfTextRenderEvent` objects:

```python
        tri = ChunkOfTextRenderEvent(canvas.graphics_state, operands[0])

        # render
        canvas._event_occurred(tri)
```

So now we know which information is being passed, and when. Let's have a look at `SimpleTextExtraction` to see how that information is processed;

```python
    def _event_occurred(self, event: Event) -> None:
        if isinstance(event, ChunkOfTextRenderEvent):
            self._render_text(event)
        if isinstance(event, BeginPageEvent):
            self._begin_page(event.get_page())
        if isinstance(event, EndPageEvent):
            self._end_page(event.get_page())
```

All implementations of `EventListener` have this `_event_occurred` method, which passes the `Event` objects it receives.
You can see `SimpleTextExtraction` only cares about the start and end of a `Page` and `ChunkOfTextRenderEvent`.

Of course, the instructions for rendering text may not be in (reading) order. So they need to be stored (until the end of a `Page`) before they can be sorted.

```python
    def _render_text(self, text_render_info: ChunkOfTextRenderEvent):

        # init if needed
        if self._current_page not in self._text_render_info_per_page:
            self._text_render_info_per_page[self._current_page] = []

        # append TextRenderInfo
        self._text_render_info_per_page[self._current_page].append(text_render_info)
```

Once the end of a `Page` is reached, the list is sorted (and any instructions that do not render text are thrown out):

```python
    def _end_page(self, page: Page):

        # get TextRenderInfo objects on page
        tris = (
            self._text_render_info_per_page[self._current_page]
            if self._current_page in self._text_render_info_per_page
            else []
        )

        # remove no-op
        tris = [x for x in tris if x._text is not None]
        tris = [x for x in tris if len(x._text.replace(" ", "")) != 0]

        # skip empty
        if len(tris) == 0:
            return

        # sort according to comparator
        sorted(tris, key=cmp_to_key(LeftToRightComparator.cmp))
```

The comparator being used sorts the `ChunkOfTextRenderEvent` objects in the expected (western) paradigm of top-to-bottom, left-to-right.

Then we need to loop over these objects and insert the `space` and `newline` character and when needed;

```python

        # iterate over the TextRenderInfo objects to get the text
        last_baseline_bottom = tris[0].get_baseline().y
        last_baseline_right = tris[0].get_baseline().x
        text = ""
        for t in tris:

            # add newline if needed
            if abs(t.get_baseline().y - last_baseline_bottom) > 10 and len(text) > 0:
                if text.endswith(" "):
                    text = text[0:-1]
                text += "\n"
                text += t._text
                last_baseline_right = t.get_baseline().x + t.get_baseline().width
                last_baseline_bottom = t.get_baseline().y
                continue

            # check text
            if t._text.startswith(" ") or text.endswith(" "):
                text += t._text
                last_baseline_right = t.get_baseline().x + t.get_baseline().width
                continue

            # add space if needed
            delta = abs(last_baseline_right - t.get_baseline().x)
            space_width = round(t.get_space_character_width_estimate_in_user_space(), 1)
            text += " " if (space_width * Decimal(0.90) < delta) else ""

            # normal append
            text += t._text
            last_baseline_right = t.get_baseline().x + t.get_baseline().width
            continue

```

finally, `SimpleTextExtraction` stores the reconstituted text (to ensure fast lookup);

```python
        # store text
        self._text_per_page[self._current_page] = text
```

### 8.7.2 Paragraph extraction and disjoint set

:mega: todo :mega:

{pagebreak}

## 8.8 Hyphenation

from wikipedia.org
> Syllabification (/sɪˌlæbɪfɪˈkeɪʃən/) or syllabication (/sɪˌlæbɪˈkeɪʃən/), also known as hyphenation, is the separation of a word into syllables, whether spoken, written or signed.
>
> The written separation into syllables is usually marked by a hyphen when using English orthography (e.g., syl-la-ble) and with a period when transcribing the actually spoken syllables in the International Phonetic Alphabet (IPA) (e.g., [ˈsɪ.lə.bᵊɫ]).
> 
> For presentation purposes, typographers may use an interpunct (Unicode character U+00B7, e.g., syl·la·ble), a special-purpose "hyphenation point" (U+2027, e.g., syl‧la‧ble), or a space (e.g., syl la ble).

At the end of a line, a word is separated in writing into parts, conventionally called "syllables", if it does not fit the line and if moving it to the next line would make the first line much shorter than the others. This can be a particular problem with very long words, and with narrow columns in newspapers.

### 5.8.1 The hyphenation problem

from wikipedia.org
> A hyphenation algorithm is a set of rules, especially one codified for implementation in a computer program, that decides at which points a word can be broken over two lines with a hyphen. For example, a hyphenation algorithm might decide that impeachment can be broken as impeach-ment or im-peachment but not impe-achment.
>
> One of the reasons for the complexity of the rules of word-breaking is that different "dialects" of English tend to differ on hyphenation[citation needed]: American English tends to work on sound, but British English tends to look to the origins of the word and then to sound. There are also a large number of exceptions, which further complicates matters.

And that's not even mentioning hyphenation in other languages.

### 8.8.2 A fast and scalable hyphenation algorithm

`borb` hyphenates text (on a `Paragraph`) if you pass it a `Hyphenation` object.
This object represents an instantiation of the aforementioned hyphenation algorithm.

The hyphenation algorithm is based on the [work of Franklin mark Liang](https://www.tug.org/docs/liang/liang-thesis.pdf), and works roughly as follows:

```
0.  input: the word 'w' to be hyphenated
1.  iterate over all possible split-positions (i) in the word w:
2.      prefix = w[0:i]
3.      suffix = w[i:]
4.      iterate over all possible suffixes of the prefix, and prefixes of the suffix:
5.          if a rule prefix-number-suffix matches:
6.              update that split position if the number is higher
7.  iterate over all split-positions (i) in the word w:
8.      if the value of the split-position is ODD:
9.          a hyphen is allowed at this position
```

The rules in aforementioned algorithm are language dependent, and are typically several thousands of rules poured into one file (e.g. `JSON`) which is loaded into a special datastructure (trie) which is optimized for this kind of lookup. 

As an example, let's look at the word "birmingham".

| b | . | i | . | r | . | m | . | i | . | n | . | g | . | h | . | a | . | m |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| b |   | i |   | r | 4 |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   | r |   | m | 3 |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   | 4 | n |   | g |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | 2 | g | h |   |   |   |   |   |
|   |   |   |   |   |   |   |   | i |   | n |   | g | 5 | h |   | a |   |   |
|   |   |   |   |   |   |   |   |   |   | n |   | g |   | h | 4 |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   | h |   | a | 2 |   |
|   | 0 |   | 0 |   | 4 |   | 3 |   | 4 |   | 2 |   | 5 |   | 4 |   | 2 |   |

After having run this algorithm, we know that "Birmingham" can be hyphenated as "Birm-ing-ham", 
since those positions yield an odd max value.

This algorithm is rather labour-intensive, so rather than running it on every word (and inserting soft-hyphens for instance),
the algorithm is only run when needed.

Whenever the `Paragraph` is performing layout, it will do the following:

```
1. Split the text into words (call this ws)
2. keep track of all lines of text that make up the paragraph, call this lines_of_text
3. for each word (w) in ws:
4.      last_line_of_text = lines_of_text[-1] + <space> + w
5.      calculate the dimensions of last_line_of_text (r)
6.      if r would fall outside the bounding box given to the paragraph:
7.          if hyphenation is enabled for this paragraph:
8.              attempt to split w
9.              if prefix of w + "-" fits:
10.                 hyphenate the word there, switch to the next line, next line starts with suffix of w
11.             else:
12.                 switch to next line, next line start with w
13.         else:
14.             switch to next line, next line starts with w 
```

This ensures hyphenation is only called when needed (rather than on every word in the sentence).

### 8.8.3 Using hyphenation in `borb`

In the next example you'll be creating a `Document` with two `Paragraph` instances.
One `Paragraph` will have hyphenation enabled, the other will not.

```python
from decimal import Decimal

from borb.pdf.canvas.layout.hyphenation.hyphenation import Hyphenation
from borb.pdf.canvas.layout.page_layout.multi_column_layout import SingleColumnLayout
from borb.pdf.canvas.layout.page_layout.page_layout import PageLayout
from borb.pdf.canvas.layout.text.paragraph import Paragraph
from borb.pdf.document.document import Document
from borb.pdf.page.page import Page
from borb.pdf.pdf import PDF


def main():

    # Document
    d: Document = Document()

    # Page
    p: Page = Page()
    d.append_page(p)

    # PageLayout
    l: PageLayout = SingleColumnLayout(p)

    # Paragraph 1
    l.add(Paragraph("Without hyphenation", font="Helvetica-bold", font_size=Decimal(20)))
    l.add(Paragraph("""
                    Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
                    Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, 
                    when an unknown printer took a galley of type and scrambled it to make a type specimen book. 
                    It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. 
                    It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, 
                    and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.    
                    """))

    # Paragraph 2
    l.add(Paragraph("With en-us hyphenation", font="Helvetica-bold", font_size=Decimal(20)))
    l.add(Paragraph("""
                    Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
                    Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, 
                    when an unknown printer took a galley of type and scrambled it to make a type specimen book. 
                    It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. 
                    It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, 
                    and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.    
                    """, hyphenation=Hyphenation("en-us")))

    # write
    with open("output.pdf", "wb") as pdf_file_handle:
        PDF.dumps(pdf_file_handle, d)


if __name__ == "__main__":
    main()

```

In the final PDF you can see the word "survived" was hyphenated as well as the word "essentially".

![enter image description here](https://raw.githubusercontent.com/jorisschellekens/borb-examples/master/chapter_008/img/borb_in_action_example_083.png)

{pagebreak}


