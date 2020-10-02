import multiprocessing


def test(num):
    print(num)


def main():
    # 创建进程池  参数为最大进程数
    po = multiprocessing.Pool(5)

    # 向进程池中添加任务
    for i in range(10):
        po.apply_async(test, args=(i,))

    # 关闭进程池，不再接收新的请求
    po.close()

    # 告诉主进程等待子进程结束，必须在close()之后
    po.join()

if __name__ == "__main__":
    main()

