from tkinter import *
from tkinter import messagebox

root = Tk()

def show_message():
    messagebox.showinfo("Information", "Hello Python!")

Button(root, text="Click Me", command=show_message).pack()

root.mainloop()