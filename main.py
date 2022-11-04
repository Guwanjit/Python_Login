from tkinter import *

root = Tk()
root.geometry("500x300")

Label(root, text="Python Registration Form", font="arial 15 bold").grid(row=0, column=3)

name = Label(root, text="Name :")
phone = Label(root, text="Phone :")
gender = Label(root, text="Gender :")
emergency = Label(root, text="Emergency :")
paymentmode = Label(root, text="Payment Mode :")

name.grid(row=1, column=2)
phone.grid(row=2, column=2)
gender.grid(row=3, column=2)
emergency.grid(row=4, column=2)
paymentmode.grid(row=5, column=2)

namevalue = StringVar
phonevalue = StringVar
gendervalue = StringVar
emergencyvalue = StringVar
paymentmodevalue = StringVar

checkvalue = IntVar

nameentry = Entry(root, textvariable=namevalue)
phoneentry = Entry(root, textvariable=phonevalue)
genderentry = Entry(root, textvariable=gendervalue)
emergencyentry = Entry(root, textvariable=emergencyvalue)
paymentmodeentry = Entry(root, textvariable=paymentmodevalue)

root.mainloop()
