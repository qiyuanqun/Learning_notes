'''
msql -u -p  这个客户端用于练习sql语句可以，但开发时没用，需要让python充当客户端

import pymysql  没有则pip安装(python2用MySQLdb)

安装软件用apt,安装python模块用pip(python模块管理工具)

python中操作mysql数据库的操作
    
    开始 --> 创建connection --> 获取cursor(游标) --> 执行sql语句 --> 关闭cursor --> 关闭connection --> 结束

    from pymysql import connection

    # 关键字参数
    conn = connection(host='localhost', port=3306, user='root', password='root', database='xxx', charset='utf8')  # 注意是utf8,没有-

    cursor = conn.cursor()

    # 查询操作
        cursor.execute('''select * from user''')  # 游标执行sql语句(sql用双引号，所以用三引号括起来方便一下，用转义不方便)，查询操作返回生效行数

        cursor.feachone()  # 从查询结果集取出一条数据，以元组形式，而且再次执行将取出下一条数据

        cursor.feachmany()  # 从结果集中取出剩下的没有取出的数据，以元组套元组的形式，可传人参数如feachmany(3),将取出下３条数据

        cursor.feachall()  # 从结果集中取出上下所以数据，即结果集，以元组套元组的形式

    # 增、删、改
    # 要动数据库，可能会返回，用提交commit（提交用连接，执行sql语句用游标）
        cursor.execute('''insert into user(name) values ("xxx")''')  # 返回生效行数
        conn.commit()  # 如果没有提交，数据库不会执行，但是会保存记录，防止提交后混乱
        
        # 如果执行sql语句后后悔了，不想提交，或者遇到异常，就用conn.rollback()回滚

难就难在sql语句怎么写
'''
