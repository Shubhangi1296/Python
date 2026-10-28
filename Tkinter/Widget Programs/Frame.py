from tkinter import *

root = Tk()

frame = Frame(root)
frame.pack()

Label(frame, text="Welcome").pack()
Button(frame, text="Submit").pack()

root.mainloop()