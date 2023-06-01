from tkinter import *
from tkinter import messagebox
from socket import *
import _thread

serVer=socket(AF_INET,SOCK_STREAM)
serVer.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
host="127.0.0.1"
port=9000
serVer.bind((host,port))
serVer.listen(5)

####################
## virable
newLine = 2



####################
####################
## Funcation
def resChat():
    global newLine, serVer
    while True:
        message = conn.recv(3000)
        Label(chatFrame, text=message.decode("utf-8"),font=("times new roman", 12), justify=RIGHT).grid(column=1,row=newLine)
        newLine +=1


def sendBtn():
    global newLine, serVer
    print(str(chatEntry.get()))# calling get() here!
    messageSinder = f"Me-> {str(chatEntry.get())}"
    Label(chatFrame, text=messageSinder,font=("times new roman", 12),justify=LEFT,fg="black").grid(column=1,row=newLine)
    newLine +=1
    chatEntry.delete(0, END)
       
####################


serVerIntf = Tk()
serVerIntf.title('chat2chat_serVer')
serVerIntf.geometry('450x350')
serVerIntf.configure(bg="#146c94")

chatFrame = Frame(serVerIntf,bg="#afd3e2")
chatFrame.place(x=5,y=5,width=435,height=295)

chatEntry = Entry(serVerIntf,font=("times new roman", 12), justify= LEFT)
chatEntry.place(x=5,y=300,width=390,height=30)

chatBtn = Button(serVerIntf,text="Send",bg="#146c94",fg="black",command=sendBtn)
chatBtn.place(x=400,y=300,width=40,height=30)

conn, addre = serVer.accept()


serVerIntf.mainloop()