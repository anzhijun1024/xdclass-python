# 简易版的udp聊天器
import socket

# 接收消息
def recv_info(udp_socket):
    recv_data = udp_socket.recvfrom(1024)
    print(recv_data)
    recv_msg = recv_data[0].decode('utf-8')
    print('接收到的消息为：',recv_msg)

# 发送消息
def send_info(udp_socket,dest_addr):
    send_data = input('请输入需要发送的内容：')
    udp_socket.sendto(send_data.encode('utf-8'),dest_addr)
    print('发送的内容是：{} 状态：成功'.format(send_data))



# 主函数入口
def main():
    # 1.创建socke对象
    udp_socket =socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 绑定本地信息及端口号
    # udp_socket.bind(('127.0.0.1',8086))
    dest_addr = ('127.0.0.1',8089)
    while True:
        # 界面显示的内容
        print('*'*30)
        print('请输入数字选择发送或者接收消息')
        print('1:发送消息')
        print('2:接收消息')
        print('*'*30)
        num = int(input('请输入数字：'))

        if num == 1:
            send_info(udp_socket,dest_addr)
        elif num == 2:
            recv_info(udp_socket)
        else:
            print('输入错误请重新输入')

if __name__ == '__main__':
    main()