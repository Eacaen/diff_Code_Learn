import os, sys
import MySQLdb
# 连接数据库
try:
    conn = MySQLdb.connect(host='localhost',user='root',passwd='',db='ADDRESSBOOKDB')       
except Exception, e:
    print (e)                               # 打印错误
    sys.exit()
cursor = conn.cursor()
sql = "insert into address(name, address) values (%s, %s)" 
values = (("张三", "北京海淀区"), ("李四", "北京海淀区"), ("王五", "北京海淀区"))
try:
    cursor.executemany(sql, values)         # 插入多条数据
except Exception, e:
    print (e)                               # 打印错误
sql = "select * from address"
cursor.execute(sql)                         # 查询数据
data = cursor.fetchall()
if data:
    for x in data:
        print (x[0], x[1])
cursor.close()                              # 关闭游标
conn.close()                            # 关闭数据库
