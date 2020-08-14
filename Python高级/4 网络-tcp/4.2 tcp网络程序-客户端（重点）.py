'''
tcp有严格的客户端和服务端之分。基于 TCP 传输方式的通信就必须事先建立连接,
则有一方是主动连接的，而另一方是被连接的； 主动连接的一方一般都是客户端, 被连接的一方一般都是服务端。


'''

'''
# 客户端流程
1、创建socket
2、输入远程的地址及端口号
3、连接服务器
4、客户端输入信息
5、客户端发送信息
6、接收服务端的消息
7、关闭socket


'''
import socket
# tcp的客户端

# 1、创建socket
tcp_socket_client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# 2、输入服务端的ip及端口号
service_ip = input('请输入地址:')
print(service_ip)
service_port = int(input('请输入端口号:'))

# 3、连接服务器
tcp_socket_client.connect((service_ip, service_port))

# 4、客户端输入消息
client_msg = input('请输入消息')

# 5、客户端发送消息
tcp_socket_client.send(client_msg.encode('utf-8'))

# 6、接收对方发过来的消息 最大接收的字节数1024字节
recv_data = tcp_socket_client.recvfrom(1024)
print('接收到内容为:%s'%recv_data[0].decode('utf-8'))


# 7、关闭套接字
tcp_socket_client.close()

