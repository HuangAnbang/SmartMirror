from Tkinter import *


root = Tk()


topFrame = Frame(root)
topFrame.pack()

bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

root.configure(background='black')
mylabel = Label(root, text = "Hello!", background='black', foreground='white')

mylabel.pack()
root.attributes("-fullscreen", True) 


root.mainloop()
