import PyPDF2
from PyPDF2.utils import PyPdfError

def merge_pdf(pdf1,pdf2, target):
    pd1 = open(pdf1, 'rb')
    pd2 = open(pdf2, 'rb')
    
    reader1 = PyPDF2.PdfFileReader(pd1)
    reader2 = PyPDF2.PdfFileReader(pd2)
    
    writer = PyPDF2.PdfFileWriter()
    
    for num in range(reader1.numPages):
        p = reader1.getPage(num)
        writer.addPage(p)
        
    for num in range(reader2.numPages):
        p = reader1.getPage(num)
        writer.addPage(p)
    
    pOutput = open(target,"wb")
    writer.write(pOutput)
    
    
    pOutput.close()
    pd1.close()
    pd2.close()
    
merge_pdf("Not_0122021_3682021.pdf","Not_0122021_3682021.pdf", "merged.pdf")
