import threading
import time


class MyThread(threading.Thread):
    def __init__(self, num):
        super(MyThread, self).__init__()
        self.num = num

    # 必须定义run()方法
    def run(self):
        for i in range(10):
            print(i + self.num)
            time.sleep(1)

    # 封装其他函数
    def other_function(self):
        pass


def main():
    '''整体流程控制'''
    t1 = MyThread(10)
    t2 = MyThread(100)
    t1.start()
    t2.start()


if __name__ == '__main__':
    main()