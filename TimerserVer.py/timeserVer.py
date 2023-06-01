import socket
import datetime

serVer= socket.socket (socket.AF_INET, socket. SOCK_STREAM)

serVer.bind((socket.gethostname(), 1998))

serVer.listen (5)


timeserVer = str(datetime.datetime.now())
globalTime=timeserVer.encode()

while True:
    conn, adrr = S.accept()
    print (f"Connection to {adrr} is established")
    conn.send(globalTime)
