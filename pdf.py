import sys
import os
import PyPDF2

merger = PyPDF2.PdfFileMerger()

#get PDFs files and path

path = sys.argv[1]
pdfs = sys.argv[2:]
os.chdir(path)


#iterate among the documents
for pdf in pdfs:
    try:
        #if doc exist then merge
        if os.path.exists(pdf):
            input = PyPDF2.PdfFileReader(open(pdf,'rb'))
            merger.append((input))
        else:
            print(f"problem with file {pdf}")

    except:
            print("cant merge !! sorry")
    else:
            print(f" {pdf} Merged !!! ")

merger.write("Merged_doc.pdf")




