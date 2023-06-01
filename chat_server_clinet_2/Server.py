from socket import *
import threading as th

chat = socket(AF_INET, SOCK_STREAM)
chat.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
ip = '127.0.0.1'
port = 7000

chat.bind((ip, port))
chat.listen(500)

def receive(session):
    while True:
        client_message = session.recv(3000).decode('UTF-8')
        print('\n Client message: ', client_message)
        if (client_message == 'close'):
            session.close()

def send(session):
    while True:
        message = input('\n Send: ').encode('UTF-8')
        session.send(message)
        if (message == 'close'):
            session.close()
            chat.close()

while True:
    session, client = chat.accept()
    print('Connection established with', client[0])
    receive_thread = th.Thread(target = receive, args = (session,))
    send_thread = th.Thread(target = send, args = (session,))
    receive_thread.start()
    send_thread.start()
    receive_thread.join()
    send_thread.join()
