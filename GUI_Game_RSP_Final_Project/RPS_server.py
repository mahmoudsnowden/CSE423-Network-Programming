import socket
from threading import *
from tkinter import *
from tkinter import scrolledtext
import sys

HOST = '127.0.0.1'
PORT = 65432

num_winFrom_1  = 0
num_loseFrom_1 = 0
num_tieFrom_1 = 0
num_winFrom_2  = 0
num_loseFrom_2 = 0
num_tieFrom_2 = 0
num_total = 0

def startServer() :
    global num_loseFrom_1, num_tieFrom_1, num_winFrom_1
    global num_loseFrom_2, num_tieFrom_2, num_winFrom_2, num_total

    print("Starting....")
    serVer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serVer.bind((HOST, PORT))
    serVer.listen()
    print("listening.....")
    
    def main_2():
        th_2 =Thread(target=stopServ)
        th_2.start()
    def stopServ():
        serVer.close()
        buttonStart.place(x=65,y=25, width=300,height=50)
        buttonStop.destroy()
        
    # buttonStart.place(x=50,y=30, width=150,height=50)
    
    buttonStop = Button(btnFrame, text="Stop", bg="#eb455f",fg="white",font=("times new roman", 15),command=main_2)
    # buttonStop.place(x=230, y=30, width=150,height=50) 
    buttonStop.place(x=65,y=25, width=300,height=50) 
    
    connFrom_1, addrFrom_1 = serVer.accept()
    print('Player 1 connected')
    statePlayerLabel_1.config(bg="#146c94",fg="white")
    connFrom_2, addrFrom_2 = serVer.accept()
    print('Player 2 connected')
    statePlayerLabel_2.config(bg="#146c94", fg="white")
    
    connFrom_1.sendall(b'You are Player One')
    connFrom_2.sendall(b'You are Player Two')
    while True:
        global num_loseFrom_1, num_tieFrom_1, num_winFrom_1
        global num_loseFrom_2, num_tieFrom_2, num_winFrom_2, num_total

        dataFrom_1 = connFrom_1.recv(1024)
        # buttonStop.config(command=main_2)

        if not dataFrom_1:
            break
        choiceFrom_1 = dataFrom_1.decode().strip().lower()

        dataFrom_2 = connFrom_2.recv(1024)
        if not dataFrom_2:
            break
        choiceFrom_2 = dataFrom_2.decode().strip().lower()

        if choiceFrom_1 == choiceFrom_2:
            
            num_tieFrom_1 +=1
            num_tieFrom_2 +=1
            num_total     +=1
            tieNumLabe_1.config(text=num_tieFrom_1)  
            tieNumLabe_2.config(text=num_tieFrom_2) 
            totalGameNumLabel.config(text=num_total)
            connFrom_1.sendall(b"It's a tie!")
            connFrom_2.sendall(b"It's a tie!")
            
        elif  (choiceFrom_1 == 'rock' and choiceFrom_2 == 'scissors') or \
                (choiceFrom_1 == 'paper' and choiceFrom_2 == 'rock') or \
                (choiceFrom_1 == 'scissors' and choiceFrom_2 == 'paper'):
                    
                num_winFrom_1  +=1
                num_loseFrom_2 +=1
                num_total      +=1
                winNumLabe_1.config(text=num_winFrom_1)  
                loseNumLabe_2.config(text=num_loseFrom_2) 
                totalGameNumLabel.config(text=num_total) 
            
                connFrom_1.sendall(b'You win!')
                connFrom_2.sendall(b'You lose!')
        elif (choiceFrom_2 == 'rock' and choiceFrom_1 == 'scissors') or \
                (choiceFrom_2 == 'paper' and choiceFrom_1 == 'rock') or \
                (choiceFrom_2 == 'scissors' and choiceFrom_1 == 'paper'):
                
                num_winFrom_2 +=1
                num_loseFrom_1 +=1
                num_total      +=1
                winNumLabe_2.config(text=num_winFrom_2) 
                loseNumLabe_1.config(text=num_loseFrom_1) 
                totalGameNumLabel.config(text=num_total)
                connFrom_2.sendall(b'You win!')
                connFrom_1.sendall(b'You lose!')
        else:
            break
############################## Main Funcation #######################
def main():
    th =Thread(target=startServer)
    th.start()
 
## Rest Game Dashbord
def RestGame():
    global num_loseFrom_1, num_tieFrom_1, num_winFrom_1
    global num_loseFrom_2, num_tieFrom_2, num_winFrom_2, num_total
    num_winFrom_1  = 0
    num_loseFrom_1 = 0
    num_tieFrom_1 = 0
    num_winFrom_2  = 0
    num_loseFrom_2 = 0
    num_tieFrom_2 = 0
    num_total = 0
    winNumLabe_1.config(text=num_winFrom_1)  
    winNumLabe_2.config(text=num_winFrom_2) 

    loseNumLabe_1.config(text=num_loseFrom_1) 
    loseNumLabe_2.config(text=num_loseFrom_2)

    tieNumLabe_1.config(text=num_tieFrom_1)  
    tieNumLabe_2.config(text=num_tieFrom_2) 

    totalGameNumLabel.config(text=num_total)
    
    statePlayerLabel_1.config(bg="white", fg="black")  
    statePlayerLabel_2.config(bg="white", fg="black")  
      
############################## GUI #######################
# Create a GUI to visualize the schedule
root = Tk()
root.title("Server")
root.geometry("450x360")
root.config(bg="#146c94")
flag = True

##Frame_

HostFrame = Frame(root,bg="#afd3e2")
HostFrame.place(x=10, y=10, width= 430, height=50)

btnFrame = Frame(root,bg="#afd3e2")
btnFrame.place(x=10, y=70, width= 430, height=100)

labelPlayerFrame = Frame(root,bg="#afd3e2")
labelPlayerFrame.place(x=10, y=180, width= 430, height=170)

#####
##Host Frame
hostLabel = Label(HostFrame, text="serVer HOST = '127.0.0.1'",font=("times new roman", 15), bg="#afd3e2", fg="black")
hostLabel.grid(column=1,row=2,padx=10, pady=20)

portLabel = Label(HostFrame, text="PORT = 65432",font=("times new roman", 15), bg="#afd3e2", fg="black")
portLabel.grid(column=2,row=2,padx=50, pady=20)
#>>>>>>>>>>>>>
##Button start 
buttonStart = Button(btnFrame, text="Start",font=("times new roman", 15), command=main,bg="#a0d8b3",)
buttonStart.place(x=65,y=25, width=300,height=50)

##label 
playerLabel_1 = Label(labelPlayerFrame, text="Player one: ",font=("times new roman", 12), bg="#afd3e2", fg="black")
playerLabel_1.grid(column=1,row=2,padx=5, pady=5)

playerLabel_2 = Label(labelPlayerFrame, text="Player two: ",font=("times new roman", 12), bg="#afd3e2", fg="black")
playerLabel_2.grid(column=1,row=3,padx=5, pady=5)

spaceLabel = Label(labelPlayerFrame, text="---------------------------------------------------------------------",font=("times new roman", 12), bg="#afd3e2", fg="black")
spaceLabel.grid(column=1,row=4,columnspan=6,padx=5)

#>>>>>>>>>>>>>>

totalGameLabel = Label(labelPlayerFrame, text="Total game: ",font=("times new roman", 12), bg="#afd3e2", fg="black")
totalGameLabel.grid(column=1,row=5,padx=5)

totalGameNumLabel = Label(labelPlayerFrame, text="0",font=("times new roman", 12), bg="#afd3e2", fg="black")
totalGameNumLabel.grid(column=2,row=5,padx=5)

restGameBtn = Button(labelPlayerFrame,text="    Rest    ",font=("times new roman", 12),bg='#19a7ce',fg="white",command=RestGame)
restGameBtn.grid(column=3,row=5,columnspan=2,padx=5)
#>>>>>>>>>>>>>>

stateLabe = Label(labelPlayerFrame,text="State",font=("times new roman", 12), bg="#afd3e2", fg="black")
stateLabe.grid(column=2, row=1,padx=10, pady=5)
               
winLabe= Label(labelPlayerFrame,text="Win",font=("times new roman", 12), bg="#afd3e2", fg="black")
winLabe.grid(column=3, row=1,padx=10, pady=5)

tieLabe = Label(labelPlayerFrame,text="Tie",font=("times new roman", 12), bg="#afd3e2", fg="black")
tieLabe.grid(column=4, row=1,padx=10, pady=5)

loseLabe = Label(labelPlayerFrame,text="Lose",font=("times new roman", 12), bg="#afd3e2", fg="black")
loseLabe.grid(column=5, row=1,padx=10, pady=5)

##DashBord

statePlayerLabel_1 = Label(labelPlayerFrame,text="on",font=("times new roman", 12), bg="white", fg="black")
statePlayerLabel_1.grid(column=2, row=2,padx=10, pady=5)


statePlayerLabel_2 = Label(labelPlayerFrame,text="on",font=("times new roman", 12), bg="white", fg="black")
statePlayerLabel_2.grid(column=2, row=3,padx=10, pady=5)
               
winNumLabe_1= Label(labelPlayerFrame,text="0",font=("times new roman", 12), bg="#afd3e2", fg="black")
winNumLabe_1.grid(column=3, row=2,padx=10, pady=5)

winNumLabe_2= Label(labelPlayerFrame,text="0",font=("times new roman", 12), bg="#afd3e2", fg="black")
winNumLabe_2.grid(column=3, row=3,padx=10, pady=5)


tieNumLabe_1 = Label(labelPlayerFrame,text="0",font=("times new roman", 12), bg="#afd3e2", fg="black")
tieNumLabe_1.grid(column=4, row=2,padx=10, pady=5)

tieNumLabe_2 = Label(labelPlayerFrame,text="0",font=("times new roman", 12), bg="#afd3e2", fg="black")
tieNumLabe_2.grid(column=4, row=3,padx=10, pady=5)

loseNumLabe_1 = Label(labelPlayerFrame,text="0",font=("times new roman", 12), bg="#afd3e2", fg="black")
loseNumLabe_1.grid(column=5, row=2,padx=10, pady=5)

loseNumLabe_2 = Label(labelPlayerFrame,text="0",font=("times new roman", 12), bg="#afd3e2", fg="black")
loseNumLabe_2.grid(column=5, row=3,padx=10, pady=5)



root.mainloop()


############################## Backup #######################

# import socket

# HOST = '127.0.0.1'
# PORT = 65432

# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.bind((HOST, PORT))
#     s.listen()
#     conn1, addr1 = s.accept()
#     print('Player 1 connected')
#     conn2, addr2 = s.accept()
#     print('Player 2 connected')

#     conn1.sendall(b'You are Player 1. Choose rock, paper, or scissors.')
#     conn2.sendall(b'You are Player 2. Choose rock, paper, or scissors.')

#     while True:
#         data1 = conn1.recv(1024)
#         if not data1:
#             break
#         choice1 = data1.decode().strip().lower()

#         data2 = conn2.recv(1024)
#         if not data2:
#             break
#         choice2 = data2.decode().strip().lower()

#         if choice1 == choice2:
#             conn1.sendall(b"It's a tie!")
#             conn2.sendall(b"It's a tie!")
#         elif (choice1 == 'rock' and choice2 == 'scissors') or \
#              (choice1 == 'paper' and choice2 == 'rock') or \
#              (choice1 == 'scissors' and choice2 == 'paper'):
#             conn1.sendall(b'You win!')
#             conn2.sendall(b'You lose!')
#         elif (choice2 == 'rock' and choice1 == 'scissors') or \
#              (choice2 == 'paper' and choice1 == 'rock') or \
#              (choice2 == 'scissors' and choice1 == 'paper'):
#             conn2.sendall(b'You win!')
#             conn1.sendall(b'You lose!')
#         else:
#             break
