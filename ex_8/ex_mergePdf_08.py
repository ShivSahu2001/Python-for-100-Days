
from PyPDF2 import PdfWriter
merger = PdfWriter()

pdfs = ['ex_8/file1.pdf', 'ex_8/file2.pdf', 'ex_8/file3.pdf']


for pdf in pdfs:
    merger.append(pdf)

merger.write('myResult.pdf')
merger.close()