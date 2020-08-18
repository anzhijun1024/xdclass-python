'''
服务端
# 创建socket
# 绑定ip及端口号
# 开始监听客服端的请求
# 拿到请求文件 打开本地文件 将文件取出
# 将文件发送到客户端
#关闭socket


'''
import socket
import sys


def get_file_connect(recv_msg):
    try:
        with open(r'.\%s' % recv_msg, 'rb') as f:
            content = f.read()
            return content
    except:
        print('输入的文件名有误无法找到该资源')


def main():
    # 创建服务端的socket
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 绑定地址
    addr = ('', 8087)
    tcp_server_socket.bind(addr)

    # 监听客户端
    tcp_server_socket.listen(128)  # backlog=5 表示积压的客户端连接请求最多5个， 超过5个，则拒绝连接

    # 等待客户端的链接
    new_socket, client_addr = tcp_server_socket.accept()

    # 接收客户端发来的数据
    recv_data = new_socket.recvfrom(1024)
    print('接收到的数据为：', recv_data[0].decode('utf-8'))
    recv_msg = recv_data[0].decode('utf-8')
    # 掉方法打开文件
    send_data = get_file_connect(recv_msg)
    # send_data = ['安智军']

    # 服务端发送内容到客户端
    print(type(send_data))

    new_socket.send(send_data)


if __name__ == '__main__':
    main()
