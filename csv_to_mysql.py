import pymysql
import pandas as pd      

db = pymysql.connect(host="localhost", user="root", password="lfr139931", database="climate")
cursor = db.cursor()
data = pd.read_csv("武大桩号.csv")



# sql = """INSERT INTO place(id, stake, name, lat, lon) VALUES (0, 'byl_bc_0_i', '野鸡山隧道北', 115.489376, 115.489376)"""

sql = "INSERT INTO place(id, stake, name, lat, lon) VALUES (%d, '%s', '%s', %f, %f)"
for index in range(2, 140):
   stake = data["公路桩号"][index]
   name = data["name"][index]
   lat = data["lat"][index]
   lon = data["lon"][index]
   try:
      cursor.execute(sql % (index, stake, name, lat, lon))
      db.commit()
   except:
      db.rollback()

# try:
#    # 执行sql语句
#    cursor.execute(sql)
#    # 提交到数据库执行
#    db.commit()
# except:
#    # 如果发生错误则回滚
#    db.rollback()

# sql = "show tables"
# res = cursor.execute(sql)

# results = cursor.fetchall()
# for res in results:
#     print(res)

db.close()