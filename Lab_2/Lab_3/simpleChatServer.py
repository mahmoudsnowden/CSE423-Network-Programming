from socket import *


## 2- Write your first simple server
serVer = socket(AF_INET, SOCK_STREAM)
localHost = "127.0.0.1"
portNum = 1998
#Bind
serVer.bind((localHost, portNum))

#Listen
serVer.listen(2)

#Accept
connection, addre = serVer.accept()
print(f"connection from {addre[0]} on port {addre[1]}")
while True:
#Receive
    dataRecv = connection.recv(1998)
    print(dataRecv.decode('utf-8'))
serVer.close()
#Send

