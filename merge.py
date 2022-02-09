from PyPDF2 import PdfFileMerger
import os
import shutil

pdfs = ["pdfs/{}".format(pdf) for pdf in os.listdir("pdfs/")]
pdfs.sort()

merger = PdfFileMerger()
    
print("Merging")
for pdf in pdfs:
    print(pdf.split('/')[1])
    try:
        pdfRead = open(pdf, 'rb')
    except Exception as e:
        pdfreadRewrite = PdfFileReader('scanner_generated.pdf',  strict = False)
        pdfwrite = PdfFileWriter()
        for page_count in range(pdfreadRewrite.numPages):
            pages = pdfreadRewrite.getPage(page_count)
            pdfwrite.addPage(pages)

        fileobjfix = open('fixedPDF.pdf', 'wb')
        pdfwrite.write(fileobjfix)
        fileobjfix.close()
        pdfRead = open('fixedPDF.pdf', 'rb')
    	    
    merger.append(pdfRead)

print("to merged.pdf")
with open("merged.pdf", "wb") as fout:
    merger.write(fout)

shutil.rmtree("pdfs/")
