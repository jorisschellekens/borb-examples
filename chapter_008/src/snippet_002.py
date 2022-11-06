def main():
    
    # create empty Document
    pdf: Document = Document()
    
    # add empty Page
    page = Page()
    pdf.add_page(page)

    # create content stream
    content_stream = Stream()
    content_stream[
        Name("DecodedBytes")
    ] = b"""
        q
        BT
        /F1 24 Tf            
        59 742 Td            
        (Lorem Ipsum) Tj
        ET
        Q
    """
    content_stream[Name("Bytes")] = zlib.compress(content_stream["DecodedBytes"], 9)
    content_stream[Name("Filter")] = Name("FlateDecode")
    content_stream[Name("Length")] = bDecimal(len(content_stream["Bytes"]))

    # set content of page
    page[Name("Contents")] = content_stream


if __name__ == "__main__":
    main()