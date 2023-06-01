import threading
import socket
host = '127.0.0.1'
port = 1998


serVer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serVer.bind((host, port))
serVer.listen()
clients = []
usErs = []


def broadcast(message):
    for client in clients:
        client.send(message)

# Function to handle clients'connections


def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            user = usErs[index]
            broadcast(f'{user} has left the chat room!'.encode('utf-8'))
            usErs.remove(user)
            break
# Main function to receive the clients connection


def serVerRecv():
    while True:
        print('Server is running and listening ...')
        client, address = server.accept()
        print(f'connection is established with {str(address)}')
        client.send('user?'.encode('utf-8'))
        user = client.recv(1024)
        usErs.append(user)
        clients.append(client)
        print(f'The user of this client is {user}'.encode('utf-8'))
        broadcast(f'{user} has connected to the chat room'.encode('utf-8'))
        client.send('you are now connected!'.encode('utf-8'))
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()



serVerRecv()
