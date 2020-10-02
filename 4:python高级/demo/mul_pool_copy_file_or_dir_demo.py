import multiprocessing
import os
import time


def copyfile(file_path, dir_path):
    file_name = os.path.basename(file_path)  # 文件名

    save_file_path = '/'.join([dir_path, file_name])  # 存储文件路径

    with open(file_path, 'rb') as f:
        with open(save_file_path, 'ab') as s:
            for line in f:
                s.write(line)


def copyhandler(po, file_or_dir_path, dir_path):
    '''处理文件或文件夹'''
    if os.path.exists(file_or_dir_path):
        if os.path.isfile(file_or_dir_path):
            # 是文件
            po.apply_async(copyfile, args=(file_or_dir_path, dir_path))

        if os.path.isdir(file_or_dir_path):
            # 是文件夹
            dir_name = os.path.basename(file_or_dir_path)
            dir_path = '/'.join([dir_path, dir_name])

            if not os.path.exists(dir_path):
                os.makedirs(dir_path)

            filename_list = os.listdir(file_or_dir_path)

            for filename in filename_list:
                file_path = '/'.join([file_or_dir_path, filename])
                copyhandler(po, file_path, dir_path)
    else:
        print('路径不存在')


def main():
    old_file_or_dir_path = '/home/luoguifu/个人笔记文件/python高级/demo'
    save_dir_path = '/home/luoguifu/个人笔记文件/python高级/复制的文件'

    po = multiprocessing.Pool(5)
    copyhandler(po, old_file_or_dir_path, save_dir_path)
    po.close()
    po.join()


if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print(end - start)