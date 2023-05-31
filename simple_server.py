from socket import *

#socket
config_server = socket(AF_INET, SOCK_STREAM)

ip_host = "127.0.0.1"
port = 7777
#bind
config_server.bind((ip_host,port))
#listen
config_server.listen(5)
print("connection....")
while True:
    connection , adder = config_server.accept()
    print(f"connection from {adder[0]}")
    data = connection.recv(2000)
    print(data.decode('utf-8'))