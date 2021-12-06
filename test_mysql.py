import pymysql
 
# 打开数据库连接
db = pymysql.connect(host="localhost", user="root", password="lfr139931", database="climate")
 
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
 
# 使用 execute()  方法执行 SQL 查询 
sql = "show tables"
res = cursor.execute(sql)

results = cursor.fetchall()
for res in results:
    print(res)

# 关闭数据库连接
db.close()