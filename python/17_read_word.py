from docx import Document


def read_doc(filename):
    doc = Document(filename)
    fullText = []
    
    for para in doc.paragraphs:
        fullText.append(para.text)
    print('\n'.join(fullText))
    
read_doc('1.docx')