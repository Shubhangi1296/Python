from tkinter import * 
master = Tk()

w = Canvas(master, width=200, height=150)
w.pack()

w.create_line(10, 10, 150, 100)

mainloop()