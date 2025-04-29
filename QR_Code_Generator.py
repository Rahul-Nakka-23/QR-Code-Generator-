# IMPORTING REQURIED LIBRARIES

import pyqrcode              # This Module helps to generate a QR Code.
import png                   # This helps to save an image in the png extension.
from pyqrcode import QRCode
import tkinter as tk         # Tkinter Module helps to create the GUI window for our project.
from tkinter import *
                               
window = Tk()                 # This method helps to create a GUI window named window.
window.geometry('300x350')    # This helps to specify the size of the window.
window.title('Rahul Project') # This helps to specify the title of the window.

'''
    --> Label() is an inbuilt function of the Tkinter Module.
        It helps in the creation of a widget that will help us display a text.
    --> pack() To display the Label(), we are going to use this method.
'''
Label(window, text="Let’s Create QR Code", font="arial 15").pack()  

s = StringVar()

def create_qrcode():
    s1 = s.get()                # get() function is used to take the input from the use 
    qr = pyqrcode.create(s1)    # this will generate a qr for the url in s1 variable  
    qr.png('myqr.png', scale=6) # using png() function we are going to save the qr with .pg extenstion 
    Label(window, text='QR Code is created and saved successfully').pack() 

Entry(window, textvariable=s, font="arial 15").pack()

'''
    --> Entry() is an inbuilt function in tkinter which creates the entry feild for the user
        to generate the qr for the user's input
    --> textvariale=s means whatever the text user enters will be stored in variable s
'''
    
Button(window, text="Create", bg="pink", command=create_qrcode).pack()
#  This is also an inbuilt function of the Tkinter Module. Button() is used to create a button on the window. 

window.mainloop()
#  This function makes the window displayed when the project is executed.
