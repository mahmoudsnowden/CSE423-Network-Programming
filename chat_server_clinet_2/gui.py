# import tkinter as tk
from tkinter import *


root = Tk()
root.title("chat2chat")
root.geometry("450x350")


def sendBtn():
    print(str(chatEntry.get()))# calling get() here!
    messageSinder = f"--> {str(chatEntry.get())}"
    # label.config(text=label.cget("text") + text + "\n")

    chatLabel.config(text=messageSinder,justify=RIGHT,fg="white")
    chatEntry.delete(0, END)


chatLabel = Label(root,font=("times new roman", 12),bg="#333c3c")
chatLabel.place(x=5,y=5,width=435,height=295)

chatEntry = Entry(root,font=("times new roman", 12), justify= LEFT)
chatEntry.place(x=5,y=300,width=390,height=30)

chatBtn = Button(root,text="Send",bg="#444488",fg="black",command=sendBtn)
chatBtn.place(x=400,y=300,width=40,height=30)

root.mainloop()