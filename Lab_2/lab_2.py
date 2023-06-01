from socket import *


serVer = socket(AF_INET,SOCK_STREAM)

## 1- send/receive buffer sizes
sendBufferSizeDefault = serVer.getsockopt(SOL_SOCKET, SO_SNDBUF)
recvBufferSizeDefault = serVer.getsockopt(SOL_SOCKET, SO_RCVBUF)
print(sendBufferSizeDefault)
print(recvBufferSizeDefault)

sendBufferSizeNew = serVer.setsockopt(SOL_SOCKET, SO_SNDBUF, 80000)
recvBufferSizeNew = serVer.setsockopt(SOL_SOCKET, SO_RCVBUF, 90000)

sendBufferSizeDefault = serVer.getsockopt(SOL_SOCKET, SO_SNDBUF)
recvBufferSizeDefault = serVer.getsockopt(SOL_SOCKET, SO_RCVBUF)
print(sendBufferSizeDefault)
print(recvBufferSizeDefault)

print("-------------------")
