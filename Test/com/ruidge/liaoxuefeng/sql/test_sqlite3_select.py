# coding=utf-8
'''
Created on 2015年2月4日

@author: zhangrui6
'''
# 导入SQLite驱动:
import sqlite3

if __name__ == "__main__":
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    # 执行查询语句:
    data = cursor.execute('select * from user where age > 50 and age < 80 ORDER BY name desc')
    for i in data:
        print str(i).encode("utf-8")
    # 获得查询结果集:
    values = cursor.fetchall()
    cursor.close()
    conn.close()
