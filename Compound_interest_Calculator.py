from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ // This is the main window
window = tk.Tk()
window.title("Compound Interest Calculator")
window.geometry("500x500")
window.resizable(False, False)
window.iconbitmap('.\images\icon.ico')
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
background_image_path = r".\images\Background.png"
dollar_image_path = r".\images\SavingiCon.png"

background_image = Image.open(background_image_path)
background_photo = ImageTk.PhotoImage(background_image)

dollar_image = Image.open(dollar_image_path)
dollar_photo = ImageTk.PhotoImage(dollar_image)

background_label = Label(window, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def calculate():
    try:
        principal = float(p1.get())
        monthly_deposit = float(p2.get())
        rate = float(p3.get()) / 100 / 12
        years = float(p4.get())
        months = years * 12
      
        amount = principal * (1 + rate)**months + monthly_deposit * (((1 + rate)**months - 1) / rate)
        
        result_label.config(text=f"Total amount after {years} years: ${amount:.2f}")
    except ValueError:
        result_label.config(text="Please enter valid numbers")
##

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
lblp1 = Label(window, text="Initial Deposit :")
lblp1.place(x=125, y=50)
p1 = Entry(window, width=20)
p1.place(x=250, y=50)
##
lblp3 = Label(window, text="Rate (%) :")
lblp3.place(x=125, y=100)
p3 = Entry(window, width=20)
p3.place(x=250, y=100)
##
lblp2 = Label(window, text="Month Deposit :")
lblp2.place(x=125, y=150)
p2 = Entry(window, width=20)
p2.place(x=250, y=150)
##
lblp4 = Label(window, text="Years :")
lblp4.place(x=125, y=200)
p4 = Entry(window, width=20)
p4.place(x=250, y=200)
##
b = Button(window, text="Calculate ", width=30, height=2,command=calculate)
b.place(x=150, y=250)
##
dollar_label = Label(window, image=dollar_photo)
dollar_label.place(x=157, y=253)
##
result_label = Label(window, text="", font=("Arial", 14))
result_label.place(x=100, y=300)


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
window.mainloop()
