from socket import *

try:
    config_clinet = socket(AF_INET, SOCK_STREAM)
    ip_host = "127.0.0.1"
    port = 7777
    config_clinet.connect((ip_host,port))
    while True:
        data_send = input("clinet: ")
        config_clinet.send(data_send.encode('utf-8'))
        data_recv = config_clinet.recv(2000)
        print(data_recv.decode('utf-8'))
    config_clinet.close
except error as e:
    print(e)
except KeyboardInterrupt:
    print("oK !")   