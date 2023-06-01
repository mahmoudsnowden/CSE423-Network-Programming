import socket
import threading

host = '127.0.0.1'
port = "1998"
userName = input("user name: ")
user = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
user.connect((host,port))

def userRecv():
    while True:
        try:
            message = user.recv(3000).decode('utf-8')
            if message == "userName?":
                user.send(userName.encode('utf-8'))
            else:
                print(message)
        except:
            print("err0r") 
            user.close()
            break
        
    
def userSend():
    while True:
        message = f'{userName}: {input("")}'
        user.send(message.encode('utf-8'))


userSendThread = threading.Thread(target=userSend)     
userRecvThread = threading.Thread(target=userRecv)

userSendThread.start()
userRecvThread.start()


            