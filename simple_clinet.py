from socket import *

config_clinet = socket(AF_INET, SOCK_STREAM)

ip_host = "127.0.0.1"
port = 8888
config_clinet.connect((ip_host,port))

config_clinet.send(b'hello world')
config_clinet.close