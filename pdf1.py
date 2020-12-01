# PDFs with Python - get number of pages, rotate pdf.
# Input - dummy.pdf
# Output - tilt.pdf

import PyPDF2

with open('dummy.pdf', 'rb') as file:
    # print(file)
    reader = PyPDF2.PdfFileReader(file)
    print(reader.numPages)  # get number of pages
    page = reader.getPage(0)
    page.rotateCounterClockwise(90)  # rotate pdf
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)
    with open('tilt.pdf', 'wb') as new_file:
        writer.write(new_file)
