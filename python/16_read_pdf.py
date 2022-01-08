from os import read
import PyPDF2

def read_pdf(filename):
    pdf = open(filename, 'rb')
    reader = PyPDF2.PdfFileReader(pdf)
    print(reader.numPages)
    obj = reader.getPage(0)
    print(obj.extractText())
    

read_pdf('Case Study - Conflict Management.pdf')