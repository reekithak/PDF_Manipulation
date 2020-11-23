#!/usr/bin/env python
# coding: utf-8

# **Pdf - To insert Signature / Images**

# - Image Space within a pdf
# - Identify Coordinates
# - Base here : X = 36x1 -> 500x1  (Finishing)
# - Base here : Y =  36y1 -> 739y1 (Finishing)
# - Finishing > Within the boundaries

# - ^ For all Pages ? ->  (Slight Differences , Adjustable )


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
#from clean import clean_

t1 = time.time()
def clean_all():
    try:
        os.remove(r"D:\working repos\Machine_Learing_PDF\ReactTrialv1\b_f1.pdf")
        os.remove(r"D:\working repos\Machine_Learing_PDF\ReactTrialv1\b_f2.pdf")
        os.remove(r"D:\working repos\Machine_Learing_PDF\ReactTrialv1\b_f3.pdf")
    except:
        pass

    try:

        os.remove(r"D:\working repos\Machine_Learing_PDF\ReactTrialv1\b1.pdf")
        os.remove(r"D:\working repos\Machine_Learing_PDF\ReactTrialv1\b2.pdf")
        os.remove(r"D:\working repos\Machine_Learing_PDF\ReactTrialv1\b3.pdf")
        os.remove(r"D:\working repos\Machine_Learing_PDF\ReactTrialv1\b4.pdf")
    except:
        pass
    
    try:
        os.rename(r"D:\working repos\Machine_Learing_PDF\ReactTrialv1\b_f4.pdf",r"D:\working repos\Machine_Learing_PDF\ReactTrialv1\signed_form.pdf")
    except:
        pass
clean_all()


def pass_pdf(pdf_fh,args,image,name,f_name):
    sig_tmp_fh = None
    pdf = PyPDF2.PdfFileReader(pdf_fh)
    writer = PyPDF2.PdfFileWriter()
    sig_tmp_filename = None
    page_num, x1, y1, width, height = [int(a) for a in args.split("x")]
    page_num = [int(x) for x in str(page_num)]
    k = 0
    for i in range(0, pdf.getNumPages()):
        page = pdf.getPage(i)
        #print(page)
        if i in page_num:
            k = 1
            #print("True")
            sig_tmp_filename = name
            c = canvas.Canvas(sig_tmp_filename, pagesize=page.cropBox)
            c.drawImage(image, x1, y1, width, height, mask='auto')
            c.showPage()
            c.save()
            #print("Done-1")
            sig_tmp_fh = open(sig_tmp_filename, 'rb')
            sig_tmp_pdf = PyPDF2.PdfFileReader(sig_tmp_fh)
            #print("Done-2")
            sig_page = sig_tmp_pdf.getPage(0)
            sig_page.mediaBox = page.mediaBox
            page.mergePage(sig_page)
            print("Finish")
            
        writer.addPage(page)
        if(k==1):
            #print("added page")
            k=0
    with open(f_name, 'wb') as fh:
            writer.write(fh)            


#Reading images
b_im = ImageReader(r"D:\working repos\Machine_Learing_PDF\ReactTrialv1\buyer_sign.png")
s_im = ImageReader(r"D:\working repos\Machine_Learing_PDF\ReactTrialv1\seller_sign.png")



'''
BASE DETAILS


BUYER:
1st : - "7x125x220x100x40"
2nd : - "7x125x150x100x40"

SELLER:
1st : - "7x340x220x100x40"
2nd : - "7x340x150x100x40"
pdf_fh = open(r"D:\working repos\Machine_Learing_PDF\ReactTrialv1\forms.pdf", 'rb')
'''


#Buyer
#1st
pdf_fh = open(r"D:\working repos\Machine_Learing_PDF\ReactTrialv1\forms.pdf", 'rb')
args = "7x125x220x100x40"
pass_pdf(pdf_fh,args,b_im,"b1.pdf","b_f1.pdf")   
#2nd
pdf_fh = open(r"D:\working repos\Machine_Learing_PDF\ReactTrialv1\b_f1.pdf", 'rb')
args = "7x125x150x100x40"
pass_pdf(pdf_fh,args,b_im,"b2.pdf","b_f2.pdf")





#seller
#1st
pdf_fh = open(r"D:\working repos\Machine_Learing_PDF\ReactTrialv1\b_f2.pdf", 'rb')
args = "7x340x220x100x40"
pass_pdf(pdf_fh,args,s_im,"b3.pdf","b_f3.pdf")   
#2nd
pdf_fh = open(r"D:\working repos\Machine_Learing_PDF\ReactTrialv1\b_f3.pdf", 'rb')
args = "7x340x150x100x40"
pass_pdf(pdf_fh,args,s_im,"b4.pdf","b_f4.pdf")

clean_all()

print("Time taken = ",time.time()-t1)
print("File saved as signed_form.pdf in the main directory :) ")
#clean_()



