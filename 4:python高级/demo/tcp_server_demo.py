import socket


def main():
    '''整体控制'''
    # 创建服务器套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # 绑定本地信息  参数为元组
    tcp_server_socket.bind(('',7788))

    # 变主动套接字为被动 这个参数没实际意义，用128即可，表示一次最多为128个客户端服务
    tcp_server_socket.listen(128)

    # 等待新的客户端连接，返回一个元组：(并专门为到达的客户端创建的新套接字服务, 到达的客户端信息——ip和端口元组)
    new_client_socket, new_client_addr = tcp_server_socket.accept()
    print(new_client_addr)

    # 接收数据  仅返回数据字节流(因为上面已经知道客户端信息了)
    recv = data = new_client_socket.recv(1024)
    
    # 发送数据  同理，只需字节流数据参数
    new_client_socket.send('已经收到数据'.encode('utf-8'))


if __name__ == '__main__':
    main()
