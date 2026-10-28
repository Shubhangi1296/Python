from tkinter import * 
main = Tk()

ourMessage = "Hi! My name is Shubhangi"

messageVar = Message(main, text=ourMessage)
messageVar.config(bg="lightgreen")
messageVar.pack()

main.mainloop()