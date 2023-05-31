from socket import *
from _thread import *
from threading import *

s = socket(AF_INET,SOCK_STREAM)
host = '127.0.0.1'
port = 7000
s.bind((host,port))
s.listen(5)
def recive(session):
    while True:
        message  = session.recv(3000).decode('utf-8')
        print('Clinet message ',message)
        if (message == 'close'):
            session.close()
    
def send(session):
    while True:
        message  = input('send:').encode('utf-8')
        session.send(message)
        print('Clinet message ',message)
        if (message == 'close'):
            session.close()
    
while True:
    session, client = s.accept()
    recive_thread = Thread(target=recive, args= (session,))
    send_thread = Thread(target=send, args= (session,))
    recive_thread.start()
    send_thread.start()
    recive_thread.join()
    send_thread.join()