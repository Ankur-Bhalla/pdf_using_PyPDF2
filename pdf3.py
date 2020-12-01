# Add Watermarker to all pdf pages to make this pdf super secret. If anybody leaks out this pdf pages then
# Watermarker will let us know who has leaked out. Generally we put Watermarker where person name has
# been written on pdf files. These Watermarker are shown on the background of the pages.
# Input - super.pdf, wtr.pdf
# Output - watermarked_output.pdf

import PyPDF2

template = PyPDF2.PdfFileReader(open('super.pdf', 'rb'))
watermark = PyPDF2.PdfFileReader(open('wtr.pdf', 'rb'))
output = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
    page = template.getPage(i)
    page.mergePage(watermark.getPage(0))  # merges the content streams of two pages into one and returns PageObject.
    output.addPage(page)

    with open('watermarked_output.pdf', 'wb') as file:
        output.write(file)
