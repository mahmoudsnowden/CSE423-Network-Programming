from socket import *
try:
    config_server = socket(AF_INET, SOCK_STREAM)
    ip_host = "127.0.0.1"
    port = 7777
    config_server.bind((ip_host,port))
    config_server.listen(5)
    print("connection....")
    connection , adder = config_server.accept()
    print(f"connection from {adder[0]}")
    while True:
        data_recv = connection.recv(2000)
        print(data_recv.decode('utf-8'))
        data_send = input("server: ")
        connection.send(data_send.encode('utf-8'))
except error as e:
    print(e)
except KeyboardInterrupt:
    print("oK !")   