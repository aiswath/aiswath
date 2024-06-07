
from tkinter import *
root = Tk()
root.geometry("300x100")

def blue():
    for widget in root.winfo_children():
        widget.pack_forget()
    label.config(text="Hello Motherfucker")
    label.pack()
    
label = Label(root,text="")

    

f = Frame(root)
b1 = Button(f,text = "Button1",bg="red",fg="black",command=blue)
b2 = Button(f,text = "Button2",bg="blue",fg="black",command=blue)
b3 = Button(f,text = "Button1",bg="green",fg="black",command=blue)
b1.pack(side=LEFT)
b2.pack(side=LEFT)
b3.pack(side=LEFT)


f.pack()
l = Label(root,text="Click any button")
l.pack()
root.mainloop()
