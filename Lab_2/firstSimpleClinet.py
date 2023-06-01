from socket import *
serVer = socket(AF_INET, SOCK_STREAM)
localHost = "127.0.0.1"
portNum = 1998
##Connect   --> one argument as ("localHost",port)
serVer.connect((localHost,portNum))

##Send      --> data to send
dataSend ="hello"
serVer.send(dataSend.encode('utf-8'))

##Receive   --> received data