import threading
import time


def test1(num):
    for i in range(10):
        print(i+num)
        time.sleep(1)


def test2(num):
    for i in range(10):
        print(i + num)
        time.sleep(1)


def main():
    '''整体流程控制'''
    thread_1 = threading.Thread(target=test1, args=(10,))
    thread_2 = threading.Thread(target=test2, args=(100,))
    thread_1.start()
    thread_2.start()

if __name__ == '__main__':
    main()