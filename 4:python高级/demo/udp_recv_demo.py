import socket


def main():
    '''接收数据整体控制'''
    udp_recv_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_recv_socket.bind(('',7788))
    recvdata = udp_recv_socket.recvfrom(1024)
    print(recvdata)
    udp_recv_socket.close()


if __name__ == '__main__':
    main()
