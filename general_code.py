import os
import time
import argparse
import tempfile
import PyPDF2
import datetime
from reportlab.pdfgen import canvas
from PIL import Image
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.utils import ImageReader
import time





args = "7x340x150x100x40"
page_num, x1, y1, width, height = [int(a) for a in args.split("x")]



page_num = [7]

#done
pdf_fh = open(r"D:\working repos\Machine_Learing_PDF\ReactTrialv1\forms.pdf", 'rb')
im = ImageReader(r"D:\working repos\Machine_Learing_PDF\ReactTrialv1\buyer_sign.png") #1440X590 -> 150X40 (width X height)


#done
sig_tmp_fh = None
pdf = PyPDF2.PdfFileReader(pdf_fh)
writer = PyPDF2.PdfFileWriter()
sig_tmp_filename = Nonek = 0
for i in range(0, pdf.getNumPages()):
        page = pdf.getPage(i)
        #print(page)
        if i in page_num:
            k = 1
            print("True")
            sig_tmp_filename = "dead.pdf"
            c = canvas.Canvas(sig_tmp_filename, pagesize=page.cropBox)
            c.drawImage(im, x1, y1, width, height, mask='auto')
            c.showPage()
            c.save()
            print("Done-1")
            sig_tmp_fh = open(sig_tmp_filename, 'rb')
            sig_tmp_pdf = PyPDF2.PdfFileReader(sig_tmp_fh)
            print("Done-2")
            sig_page = sig_tmp_pdf.getPage(0)
            sig_page.mediaBox = page.mediaBox
            page.mergePage(sig_page)
            print("Finish")
            
        writer.addPage(page)
        if(k==1):
            print("added page")
            k=0
            

with open("dead_test_1.pdf", 'wb') as fh:
        writer.write(fh)
