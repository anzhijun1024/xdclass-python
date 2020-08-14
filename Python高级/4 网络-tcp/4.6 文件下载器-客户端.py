'''
客户端负责请求 发送内容
# 创建socket
# 绑定地址及端口号
# 输入文件名
# 将文件名发送给服务端
# 接收文件
# 关闭socket

'''
import socket
def main():

    # 创建socket
    tcp_client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    # 输入地址及端口号并链接
    client_ip =input('请输入服务端的地址')
    client_port = int(input('请输入服务端的端口号'))
    tcp_client.connect((client_ip,client_port))
    print('服务器连接成功')

    #输入要下载的文件名称
    send_data= input('请输入要下载的文件名称')
    tcp_client.send(send_data.encode('utf-8'))

    # 接收服务器的数据
    recv_data = tcp_client.recvfrom(1024)

    print('内容是：',recv_data[0].decode('utf-8'))

    # 传输完成关闭套接字
    tcp_client.close()


if __name__ == '__main__':
    main()