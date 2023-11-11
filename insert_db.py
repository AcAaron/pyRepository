from  pymysql import Connection
import multithread as m
conn = Connection(
    host='localhost',
    port=3306,
    user='root',
    password='123456',
    autocommit=True
)
cursor=conn.cursor()
conn.select_db('world')
m.multi()
for i in m.spider.li:
    sql=f'INSERT INTO q(title) VALUE("{i}")'
    cursor.execute(sql)

conn.close()