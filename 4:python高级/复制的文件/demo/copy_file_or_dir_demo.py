import os
import time


def copyfile(old_file_path, save_dir_path):
    file_name = os.path.basename(old_file_path)  # 文件名

    new_file_path = '/'.join([save_dir_path, file_name])

    with open(old_file_path, 'rb') as f1:
        with open(new_file_path, 'ab') as f2:
            for line in f1:
                f2.write(line)


def copyhandler(file_or_dir_path, save_dir_path):
    '''
    处理文件或文件夹
    :param file_or_dir_path: str  文件或文件夹
    :param save_dir_path: str  存储文件夹
    '''
    if os.path.exists(file_or_dir_path):
        # 文件或文件夹存在
        if os.path.isfile(file_or_dir_path):
            # 文件
            copyfile(file_or_dir_path, save_dir_path)
        if os.path.isdir(file_or_dir_path):
            # 文件夹
            # 文件夹名字
            dir_name = os.path.basename(file_or_dir_path)

            # 更新存储文件夹
            save_dir_path = '/'.join([save_dir_path, dir_name])

            if not os.path.exists(save_dir_path):
                # 存储文件夹不存在，创建它
                os.makedirs(save_dir_path)

            # 文件夹下所有文件或文件夹
            filename_list = os.listdir(file_or_dir_path)
            for filename in filename_list:
                # 更新文件或文件夹
                file_or_dir_path = '/'.join([file_or_dir_path, filename])
                copyhandler(file_or_dir_path, save_dir_path)
    else:
        # 文件或文件夹不存在
        print('路径不存在')


def main():
    # 文件或文件夹
    file_or_dir_path = '/home/luoguifu/个人笔记文件/python高级/demo'

    # 存储文件夹
    save_dir_path = '/home/luoguifu/个人笔记文件/python高级/复制的文件'

    copyhandler(file_or_dir_path, save_dir_path)


if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print(end - start)
