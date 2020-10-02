import socket


def main():
    # 创建套接字
    tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 连接服务器  参数为元组
    tcp_client_socket.connect(('127.0.0.1', 7788))

    # 发送数据
    tcp_client_socket.send('向服务器发送数据'.encode('utf-8'))

    # 接收数据
    recv_data = tcp_client_socket.recv(1024)
    print(recv_data.decode('utf-8'))

    # 关闭套接字
    tcp_client_socket.close()


if __name__ == '__main__':
    main()
