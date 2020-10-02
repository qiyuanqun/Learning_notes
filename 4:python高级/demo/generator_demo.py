from collections import Iterable, Iterator


def generator(num):
    '''生成从0到num的序列'''
    current_num = 0
    while True:
        if current_num <= num:
            yield current_num
            current_num += 1
        else:
            raise StopIteration


if __name__ == '__main__':
    a = (i for i in range(10))
    for i in a:
        print(i)

    g = generator(10)
    print(isinstance(g, Iterable))  # True
    print(isinstance(g, Iterator))  # True
    for i in g:
        print(i)