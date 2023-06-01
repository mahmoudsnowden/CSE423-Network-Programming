from tkinter import *
from tkinter import messagebox
from socket import *
import _thread

usEr=socket(AF_INET,SOCK_STREAM)
host="127.0.0.1"
port=9000
usEr.connect((host,port))


####################
## virable
newLine = 2



####################
####################
## Funcation
def resvChat():
    global newLine, usEr
    while True:
        message = usEr.recv(3000)
        messageRecv = f"usEr--> {message.decode('utf-8')}"
        print(messageRecv)
        Label(chatFrame, text=messageRecv,font=("times new roman", 12), justify=RIGHT).grid(column=1,row=newLine)
        newLine +=1

_thread.start_new_thread(resvChat,())

def sendBtn():
    global newLine, usEr
    print(str(chatEntry.get()))# calling get() here!
    messageSinder = f"Me-> {str(chatEntry.get())}"
    usEr.send(str(chatEntry.get()))
    Label(chatFrame, text=str(chatEntry.get()),font=("times new roman", 12),justify=LEFT,fg="black").grid(column=1,row=newLine)
    newLine +=1
    chatEntry.delete(0, END)
    
def sendBtn():
    global newLine, serVer
    print(str(chatEntry.get()))# calling get() here!
    messageSinder = f"Me-> {str(chatEntry.get())}"
    Label(chatFrame, text=messageSinder,font=("times new roman", 12),justify=LEFT,fg="black").grid(column=1,row=newLine)
    newLine +=1
    chatEntry.delete(0, END)
       
####################


userVerIntf = Tk()
userVerIntf.title('chat2chat_USER')
userVerIntf.geometry('450x350')
userVerIntf.configure(bg="#146c94")

chatFrame = Frame(userVerIntf,bg="#afd3e2")
chatFrame.place(x=5,y=5,width=435,height=295)

chatEntry = Entry(userVerIntf,font=("times new roman", 12), justify= LEFT)
chatEntry.place(x=5,y=300,width=390,height=30)

chatBtn = Button(userVerIntf,text="Send",bg="#146c94",fg="black",command=sendBtn)
chatBtn.place(x=400,y=300,width=40,height=30)

# conn, addre = usEr.accept()


userVerIntf.mainloop()