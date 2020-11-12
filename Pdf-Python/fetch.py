from __future__ import absolute_import
from firebase import Firebase 
from pyrebase import pyrebase
import webbrowser


config = {
  "apiKey": "yourapikey",
  "authDomain": "try-python-pull.firebaseapp.com",
  "databaseURL": "https://try-python-pull.firebaseio.com",
  "storageBucket": "try-python-pull.appspot.com"
}

firebase = pyrebase.initialize_app(config)

storage = firebase.storage()

storage.child("applsci-10-01245-v2.pdf").download(filename ="new_pdf.pdf",path=r"D:\working repos\Machine_Learing_PDF\ReactTrialv1\Pdf-Python")
webbrowser.open_new("new_pdf.pdf")