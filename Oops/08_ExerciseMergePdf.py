# Write a program to manipulate pdf files using pyPDF.
# Your programs should be able to merge multiple pdf files into a single pdf. 
# You are welcome to add more functionalities pypdf is a free and 
# open-source pure-python PDF library capable of splitting, merging, 
# cropping, and transforming the pages of PDF files. It can also add custom data, 
# viewing options, and passwords to 
# PDF files. pypdf can retrieve text and metadata from PDFs as well.


# importing pypdf 

from pypdf import PdfWriter
import os





# give the directiory where pdf present
def mergePdf(directiory):

    pdfList = os.listdir(directiory)
    merger = PdfWriter()
    outputList=[]
    for file in pdfList:
        absfile = os.path.join(directiory, file)
        # print(absfile)
        outputList.append(absfile)

    # print(outputList)
    
    for pdf in outputList:
        merger.append(pdf)

    merger.write(f"{directiory}/Merged-Pdf.pdf")
    merger.close()


print("Welcome to pdf Merging System!")
print("Enter your Directiory where all Pdfs are present Note:default directiory given")
directiory = "/home/santosh/Desktop/Python/Python/Oops/PdfContainerFolder"
mergePdf(directiory)

# pdfList = os.listdir(directiory)
# print(pdfList)