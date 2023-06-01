from socket import *
import threading as th

chat = socket(AF_INET, SOCK_STREAM)
server_ip = '127.0.0.1'
server_port = 7000

chat.connect((server_ip, server_port))

def receive(chat):
    while True:
        server_message = chat.recv(3000).decode('UTF-8')
        print('Server message: ', server_message)
        if (server_message == 'close'):
            chat.close()

receive_thread = th.Thread(target = receive, args = (chat,))
receive_thread.start()

while True:
    message = input('Send: ').encode('UTF-8')
    chat.send(message)
    if (message == 'close'):
        chat.close()
        break
