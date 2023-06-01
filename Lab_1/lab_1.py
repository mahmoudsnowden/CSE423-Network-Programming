import socket

## 1- Machine`s name and IPv4 address

pcName = socket.gethostname()
ipv4 = socket.gethostbyname(pcName)

print("Machine naem --> "+pcName)

print("Machine Port --> "+ipv4)
print("----------------------")

## 2- Get Service name, given the port and protocol
port = 23
serviceName = socket.getservbyport(port,"tcp") #"tcp" --> optional
print(serviceName)
print("----------------------")

## 3- Get Port number, given the service name and protocol
servName = "ssh"
port = socket.getservbyname(servName,"tcp") #"tcp" --> optional
print(port)
print("---------")

## 4- Converting intergers to and from host to network byte order 
data = 12345
long_data = socket.htonl(data)
short_data= socket.htons(data)
print(long_data )
print(short_data)
print("----------------------")

## 5- Set and get timeout
serVer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serVer.settimeout(44)
print(serVer.gettimeout())
print("----------------------")

## 6- Converting an IPv4 address to different formats
ipAddress = "127.0.0.1"
packingIpAddress = socket.inet_aton(ipAddress)
print(packingIpAddress)

from binascii import hexlify
print(hexlify(packingIpAddress))

IPv4 = socket.inet_ntoa(packingIpAddress)
print(IPv4)
print("----------------------")


