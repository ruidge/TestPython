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
    
    r = cursor.execute('drop table if exists user')
    cursor.close()
    conn.close()
