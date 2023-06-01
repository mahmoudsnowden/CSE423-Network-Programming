import socket
from tkinter import *
HOST = '127.0.0.1'
PORT = 65432

num_win  = 0
num_lose = 0
num_tie  = 0
num_total = 0
############################# GUI #######################
# Create a GUI to visualize the schedule
root = Tk()
root.title("Player ")
root.geometry("450x380")
root.config(bg="#146c94")
##################
btnFrame = Frame(root,bg="#afd3e2")
btnFrame.place(x=10, y=10, width= 430, height=150)

labelFrame = Frame(root,bg="#afd3e2")
labelFrame.place(x=10, y=165, width= 430, height=200)


##################
cliNet = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliNet.connect((HOST, PORT))

data = cliNet.recv(1024)
player_num = data.decode()
player_status = " "

##################

rockImg =       PhotoImage(file = r"F:\allData\4th\4.2 th_2023_Labs\networkProgrammaning\GUI_Game\rock.png")
rockImg_2 =     PhotoImage(file = r"F:\allData\4th\4.2 th_2023_Labs\networkProgrammaning\GUI_Game\rock_2.png")
paperImg =      PhotoImage(file = r"F:\allData\4th\4.2 th_2023_Labs\networkProgrammaning\GUI_Game\paper.png")
paperImg_2 =    PhotoImage(file = r"F:\allData\4th\4.2 th_2023_Labs\networkProgrammaning\GUI_Game\paper_2.png")
scissorsImg =   PhotoImage(file = r"F:\allData\4th\4.2 th_2023_Labs\networkProgrammaning\GUI_Game\scissors.png")
scissorsImg_2 = PhotoImage(file = r"F:\allData\4th\4.2 th_2023_Labs\networkProgrammaning\GUI_Game\scissors_2.png")



def btnRock():
    global num_lose, num_tie, num_win, num_total

    choice = "rock"
    cliNet.sendall(choice.encode())
    data = cliNet.recv(1024)
    player_status = data.decode()
    playerStatus.config(text=player_status)
    if player_status == 'You win!':
        num_win +=1
        num_total +=1
        numWin.config(text=num_win)
        numTotal.config(text=num_total)
        playerStatus.config(bg="#a0d8b3",fg="black")
        
    elif player_status == 'You lose!':
        num_lose +=1
        num_total +=1
        numLose.config(text=num_lose)
        numTotal.config(text=num_total)
        playerStatus.config(bg="#eb455f",fg="white")
    # else player_status == "It's a tie!":
    else:
        num_tie +=1
        num_total +=1
        numTie.config(text=num_tie)
        numTotal.config(text=num_total)
        playerStatus.config(bg="#444444", fg="white")
    
def btnPaper():
    global num_lose, num_tie, num_win, num_total

    choice = "paper"
    cliNet.sendall(choice.encode())
    data = cliNet.recv(1024)
    player_status = data.decode()
    playerStatus.config(text=player_status)
    if player_status == 'You win!':
        num_win +=1
        num_total +=1
        numWin.config(text=num_win)
        numTotal.config(text=num_total)
        playerStatus.config(bg="#a0d8b3",fg="black")
        
    elif player_status == 'You lose!':
        num_lose +=1
        num_total +=1
        numLose.config(text=num_lose)
        numTotal.config(text=num_total)
        playerStatus.config(bg="#eb455f",fg="white")
    # else player_status == "It's a tie!":
    else:
        num_tie +=1
        num_total +=1
        numTie.config(text=num_tie)
        numTotal.config(text=num_total)
        playerStatus.config(bg="#444444", fg="white")

    
def btnScissors():
    global num_lose, num_tie, num_win, num_total

    choice = "scissors"
    cliNet.sendall(choice.encode())
    data = cliNet.recv(1024)
    player_status = data.decode()
    playerStatus.config(text=player_status)
    if player_status == 'You win!':
        num_win +=1
        num_total +=1
        numWin.config(text=num_win)
        numTotal.config(text=num_total)
        playerStatus.config(bg="#a0d8b3",fg="black")
    elif player_status == 'You lose!':
        num_lose +=1
        num_total +=1
        numLose.config(text=num_lose)
        numTotal.config(text=num_total)
        playerStatus.config(bg="#eb455f",fg="white")
    # else player_status == "It's a tie!":
    else:
        num_tie +=1
        num_total +=1
        numTie.config(text=num_tie)
        numTotal.config(text=num_total)
        playerStatus.config(bg="#444444", fg="white")
 #to rest Game       
def restGame():
    global num_lose, num_tie, num_win, num_total
    
    num_tie   =0
    num_win   =0
    num_lose  =0
    num_total =0
    
    numTie.config(text=num_tie)
    numWin.config(text=num_win)
    numLose.config(text=num_lose)
    numTotal.config(text=num_total)
        
            
buttonRock = Button(btnFrame, text="Start", bg="#19a7ce",command=btnRock)
buttonRock.grid(column=1, row=2, pady=5,padx=5)
buttonRock.config(image=rockImg)

buttonPaper = Button(btnFrame, text="Start",bg='#19a7ce', command=btnPaper)
buttonPaper.grid(column=2, row=2, pady=5,padx=5)
buttonPaper.config(image=paperImg)

buttonScissors = Button(btnFrame, text="Start",bg='#19a7ce', command=btnScissors)
buttonScissors.grid(column=3, row=2, pady=5,padx=5)
buttonScissors.config(image=scissorsImg)

#.........................................................
##label Frame

playerNum = Label(labelFrame,text="You are Player Two", font=("times new roman", 15),bg="#afd3e2", fg="black")
playerNum.grid( column=5,row=1,columnspan=3,padx=55, pady=5)
playerNum.config(text=player_num)

playerStatus = Label(labelFrame,text = "Win", font=("times new roman", 15), borderwidth=5, bg="#afd3e2", fg="black")
playerStatus.grid( column=5,row=2,columnspan=3,padx=5, pady=5)
playerStatus.config(text=player_status)


##
Win_label = Label(labelFrame, text="Win: ",font=("times new roman", 15), bg="#afd3e2", fg="black")
Win_label.grid( column=1,row=3,padx=0, pady=5)

numWin = Label(labelFrame,font=("times new roman", 15), bg="#444444", fg="white")
numWin.grid( column=2,row=3,padx=5, pady=5)
numWin.config(text=num_win)

##
Tie_label = Label(labelFrame, text="Tie: ",font=("times new roman", 15), bg="#afd3e2", fg="black")
Tie_label.grid( column=1,row=4,padx=5, pady=5)

numTie = Label(labelFrame, text="....",font=("times new roman", 15), bg="#444444", fg="white")
numTie.grid( column=2,row=4,padx=5, pady=5)
numTie.config(text=num_tie)

##
Lose_label = Label(labelFrame, text="Lose: ",font=("times new roman", 12),bg="#afd3e2", fg="black")
Lose_label.grid( column=1,row=5,padx=5, pady=5)

numLose = Label(labelFrame, text="....",font=("times new roman", 15), bg="#444444", fg="white")
numLose.grid( column=2,row=5,padx=5, pady=5)
numLose.config(text=num_lose)


##
Total_label = Label(labelFrame, text="Total: ",font=("times new roman", 15), bg="#afd3e2", fg="black")
Total_label.grid( column=8,row=3,padx=0, pady=5)

numTotal = Label(labelFrame, text="....",font=("times new roman", 12),bg="#afd3e2", fg="black")
numTotal.grid( column=8,row=4)
numTotal.config(text=num_total)

##
btnRest = Button(labelFrame, text=" Rest ",font=("times new roman", 15),bg='#19a7ce',fg="white", command=restGame)
btnRest.grid(column=8, row=5,pady=0,padx=0)




#>>>>>>>>>>>>>>>>>>>>>>>>

root.mainloop()

