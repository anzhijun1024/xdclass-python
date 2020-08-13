

import socket
# socket.socket(AddressFamily,Type)


import socket
# 创建一个udp socket 的套接字
s= socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s.close()


# 创建一个tcp socket (tcp套接字)
s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.close()
