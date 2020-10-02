import multiprocessing
import time


def download_from_web(q):
    '''下载数据'''
    # 模拟从网上下载的数据
    data = [11,22,33,44]

    for temp in data:
        # 向对列中写数据
        q.put(temp)

    print('下载结束')


def analysis(q):
    '''数据处理'''
    waitting_analysis_data = list()  # 空列表用list()可读性强

    while True:
        # 从队列中获取数据
        data = q.get()
        waitting_analysis_data.append(data)
        if q.empty():
            break

    # 模拟数据处理
    print(waitting_analysis_data)


def main():
    # 创建一个队列
    q = multiprocessing.Queue(3)  # 3代表队列最多存放3个数据，不写则由操作系统决定

    # 创建多进程，将队列的引用当做实参传入
    p1 = multiprocessing.Process(target=download_from_web,args=(q,))
    p2 = multiprocessing.Process(target=analysis, args=(q,))
    p1.start()
    p2.start()


if __name__ == '__main__':
    main()