#This module contains all the functions for working with PDF documents.
import PyPDF2 as pf

# Step 1 Read pdf into a variable
pdf = pf.PdfReader(r'C:\Users\richs\PycharmProjects\HexTree\hextree_stirling_pdf_exploit\https___www_l2otmraw2yavo_hexbirch_com_a_html.pdf')

# Step 2 "The process of traversing the PDF tree structure"

catalog = pdf.trailer['/Root']
fDetail = catalog['/Names']['/EmbeddedFiles']['/Names']
soup = fDetail[1].get_object()

# Step 3 Stream data to a variable for further use
file = soup['/EF']['/F'].get_data()
print(file)
#data = bytearray(file).replace(b'\n', b' ')
#print(data)
