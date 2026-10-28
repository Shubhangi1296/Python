from tkinter import *

root = Tk()

lf = LabelFrame(root, text="Student Details")
lf.pack(padx=10, pady=10)

Label(lf, text="Name").pack()
Entry(lf).pack()

root.mainloop()