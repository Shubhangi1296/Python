from tkinter import *

root = Tk()

pw = PanedWindow(root, orient=HORIZONTAL)
pw.pack(fill=BOTH, expand=True)

pw.add(Label(pw, text="Left Pane"))
pw.add(Label(pw, text="Right Pane"))

root.mainloop()