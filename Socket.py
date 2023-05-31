from socket import *
# host_name = gethostname()
# ip = gethostbyname(host_name)
# ip_site = gethostbyname('google.com')
# serbyport = getservbyport(22)
# serbyportAndProtocol = getservbyport(22,'tcp')
# portbyser = getservbyname(serbyport)

# print(host_name)
# print(ip)
# print(ip_site)
# print(serbyport)
# print(serbyportAndProtocol)
# print(portbyser)

###############################
##### Set and Get timeout #####
###############################

# c = socket(AF_INET,SOCK_STREAM) #AddressFamily = ipv4  , stream = tcp
# c.settimeout(50)
# print(c.gettimeout())

#########################################################
##### Set and Get socket`s send/receive buffer size #####
#########################################################

c = socket(AF_INET,SOCK_STREAM) #AddressFamily = ipv4  , stream = tcp
send_buffer_size = c.getsockopt(SOL_SOCKET,SO_SNDBUF)
recv_buffer_size = c.getsockopt(SOL_SOCKET,SO_RCVBUF)

print(recv_buffer_size)
print(send_buffer_size)

add_send_buffer_size = c.setsockopt(SOL_SOCKET,SO_SNDBUF,70000)
send_buffer_size = c.getsockopt(SOL_SOCKET,SO_SNDBUF)
print(send_buffer_size)
