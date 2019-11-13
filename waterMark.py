from PyPDF2 import PdfFileWriter, PdfFileReader
import sys
import os

#get input, output and waterMark files and cd to that location
input = sys.argv[1]
output = sys.argv[2]
water_mark = sys.argv[3]
path = sys.argv[4]
if not os.path.exists(path):
    os.mkdir(path)
os.chdir(path)

#Get the Water Mark page
watermark_obj = PdfFileReader(water_mark)
watermark_page = watermark_obj.getPage(0)

# Create objects for Input pages
input_reader_obj = PdfFileReader(input)
output_writer_obj = PdfFileWriter()

# Water Marking all the input file pages

for page_num in range(input_reader_obj.getNumPages()):
    page = input_reader_obj.getPage(page_num)
    page.mergePage(watermark_page) # MergePage merges the contents of 2 pages, should be acted on a page object- page1.mergePage(page2)
    output_writer_obj.addPage(page)

with open(output, "wb") as Out:
    output_writer_obj.write(Out)

print("All Done !!!")


