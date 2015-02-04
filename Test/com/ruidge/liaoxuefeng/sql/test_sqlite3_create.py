# coding=utf-8
'''
Created on 2015年2月4日

@author: zhangrui6
'''
# 导入SQLite驱动:
import sqlite3

if __name__ == "__main__":
    # 连接到SQLite数据库
    # 数据库文件是test.db
    # 如果文件不存在，会自动在当前目录创建:
    conn = sqlite3.connect('test.db')
    
    # 创建一个Cursor:
    cursor = conn.cursor()
    # 执行一条SQL语句，创建user表:
    cursor.execute(r'create table if not exists user (id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(20),age INTEGER)')
    # 继续执行一条SQL语句，插入一条记录:
    for i in range(1, 101):
        sqlstr = r'insert into user (name,age) values ("tom_%s",%s)' % (i, i)
        cursor.execute(sqlstr)
    # 通过rowcount获得插入的行数:
    print cursor.rowcount
    # 关闭Cursor:
    cursor.close()
    # 提交事务:
    conn.commit()
    # 关闭Connection:
    conn.close()
