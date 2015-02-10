# coding=utf-8
'''
Created on 2015年2月10日

@author: zhangrui6
'''
import mysql.connector

if __name__ == "__main__":
    conn = mysql.connector.connect(user='root', password='password', database='ruidge', use_unicode=True)
    cursor = conn.cursor()
    # 创建user表:
    cursor.execute('create table if not exists user (id int primary key auto_increment,uid varchar(20), name varchar(20))')
    # 插入一行记录，注意MySQL的占位符是%s:
    cursor.execute('insert into user (uid, name) values (%s, %s)', ['1', 'Michael'])
    print cursor.rowcount
    # 提交事务:
    conn.commit()
    cursor.close()
    # 运行查询:
    cursor = conn.cursor()
#     cursor.execute('select * from user where id = %s', '1')
    cursor.execute('select * from user')
    values = cursor.fetchall()
    print values
    # 关闭Cursor和Connection:
    cursor.close()
    conn.close()
