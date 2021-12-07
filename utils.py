import numpy

# 返回风力和风向
def uv2wsd(x, y):
    import numpy as np
    ws = np.sqrt(x ** 2 + y ** 2)
    wd = np.arctan2(y, x)
    wd = np.degrees(wd)  # 将弧度转化为角度
    return (ws, wd)


def test_mysql():
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

if __name__ == "__main__":
    ws, wd = uv2wsd(10, -10)
    print(ws, wd)

    test_mysql()