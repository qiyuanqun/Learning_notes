import socket


def main():
    '''发送数据主体控制'''
    udp_send_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_send_socket.sendto('辉煌科技'.encode('utf-8'),('127.0.0.1', 7788))
    udp_send_socket.close()


if __name__ == '__main__':
    main()
