import os


def clean_():
    try:

        os.remove("b_f3.pdf")
    except:
        pass
    try:
        os.remove("b_f4.pdf")
    except:
        pass
    try:
        os.remove("b3.pdf")
    except:
        pass
    try:
        os.remove("b4.pdf")
    except:
        pass
clean_()