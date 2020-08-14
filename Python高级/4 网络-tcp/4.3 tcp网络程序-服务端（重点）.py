

'''
# tcp 服务器流程
# 1、创建套接字
#2、绑定ip和端口号
#3、listen开始监听
# 4、等待客户端的连接
#5、接收及发送消息
# 6、关闭套接字
'''

import socket
# 1、创建套接字
tcp_socket_service =socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# 本地信息
address = ('192.168.2.189',8088)

# 绑定
tcp_socket_service.bind(address)

# 3、开始监听服务端的请求
tcp_socket_service.listen(5)# backlog=5 表示积压的客户端连接请求最多5个， 超过5个，则拒绝连接

# 如果有新的客户端来连接服务器，那么就产生一个新的套接字专门为这个客户端服务
# new_socket用来为这个客户端服务
# tcp_server_socket就可以省下来专门等待其他新客户端的连接
new_socket,client_addr= tcp_socket_service.accept()

# 4、接收客户端发来的消息
client_recv = new_socket.recvfrom(1024)
print('接收到的数据为：',client_recv[0].decode('utf-8'))

# 5、服务端发送消息
send_data=input('请输入要发送的内容')
new_socket.send(send_data.encode('utf-8'))


# 6、关闭socket
new_socket.close()