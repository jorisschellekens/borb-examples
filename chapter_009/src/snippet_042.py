from borb.pdf import Document
from borb.pdf import Page
from borb.pdf import PDF
from borb.pdf import SingleColumnLayout
from borb.pdf import PageLayout
from borb.pdf import Paragraph

import dropbox

from decimal import Decimal
from pathlib import Path

import io


def dropbox_connect() -> dropbox.dropbox_client.Dropbox:
    """
    This function connects to Dropbox and returns the API connection
    :return:    a connection to the Dropbox API
    """
    try:
        dbx = dropbox.Dropbox('<your access key>')
    except AuthError as e:
        print('Error connecting to Dropbox with access token: ' + str(e))
    return dbx


def create_pdf() -> Document:
    """
    This function creates a PDF document containing the "Hello World" text.
    :return:    a borb.pdf.Document
    """

    # create Document
    doc: Document = Document()

    # create Page
    page: Page = Page()
    doc.add_page(page)

    # PageLayout
    layout: PageLayout = SingleColumnLayout(page)

    # add Paragraph
    layout.add(Paragraph("Hello World"))

    # return
    return doc


def document_to_bytes(pdf: Document) -> bytes:
    """
    This function converts a borb.pdf.Document to bytes
    :param pdf:     the input borb.pdf.Document
    :return:        the output bytes
    """
    buffer = io.BytesIO()
    PDF.dumps(buffer, pdf)
    buffer.seek(0)
    return buffer.getvalue()


if __name__ == '__main__':

    # set up connection
    dbx:dropbox.dropbox_client.Dropbox = dropbox_connect()
    print(dbx)

    # create PDF
    pdf: Document = create_pdf()

    # upload
    dbx.files_upload(document_to_bytes(pdf),
                     '/pdfs/hello_world.pdf',
                     mode=dropbox.files.WriteMode("overwrite"))
