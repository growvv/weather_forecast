from ast import walk
import pymysql
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import config
from utils import uv2wsd
 
# db = pymysql.connect(host="localhost", user="root", password="lfr139931", database="climate")
# cursor = db.cursor()

# SELECT * FROM place WHERE name LIKE '%西羊%';
def query_place(place_name, limit=1):
    sql = "SELECT * FROM place WHERE name LIKE '%" + place_name + "%'"
    db = pymysql.connect(host="localhost", user="root", password="lfr139931", database="climate")
    cursor = db.cursor()
    cursor.execute(sql)
    results = cursor.fetchall()
    name_latlon = {}
    names = []
    for result in results:
        name_latlon[result[2]] = ({"stake": result[1], "name": result[2], "lat": result[3], "lon":result[4]})
        names.append(result[2])

    # print(name_latlon)
    results = process.extract(place_name, names, limit=limit)
    ret = []
    for result in results:
        ret.append(name_latlon[result[0]])

    db.close()
    return ret


def query_climate(time, lat, lon, weather_element):
    # solve(time)
    # solve(lat)
    # solve(lon)
    weather_element = process.extract(weather_element, config.weather_elements, limit=1)
    weather_element = weather_element[0][0]
    # print(weather_element)

    sql = ""
    db = pymysql.connect(host="localhost", user="root", password="lfr139931", database="climate")
    cursor = db.cursor()
    
    if weather_element == "降水量":
        weather_element = config.climap[weather_element]
        sql = "SELECT precipitations FROM weather WHERE time=%f and lat=%f and lon=%f"
        cursor.execute(sql % (time, lat, lon))
        res = cursor.fetchone()[0]
    elif weather_element == "相对湿度":
        weather_element = config.climap[weather_element]
        sql = "SELECT relative_humidity FROM weather WHERE time=%f and lat=%f and lon=%f"
        cursor.execute(sql % (time, lat, lon))
        res = cursor.fetchone()[0]
    elif weather_element == "温度":
        weather_element = config.climap[weather_element]
        sql = "SELECT temperature FROM weather WHERE time=%f and lat=%f and lon=%f"
        cursor.execute(sql % (time, lat, lon))
        res = cursor.fetchone()[0]
    else:
        u_wind = config.climap["u风"]
        v_wind = config.climap["v风"]
        sql = "SELECT u_component_of_wind FROM weather WHERE time=%f and lat=%f and lon=%f"
        cursor.execute(sql % (time, lat, lon))
        u_wind = cursor.fetchone()[0]

        sql = "SELECT v_component_of_wind FROM weather WHERE time=%f and lat=%f and lon=%f"
        cursor.execute(sql % (time, lat, lon))
        v_wind = cursor.fetchone()[0]

        ws, wd = uv2wsd(u_wind, v_wind)
        res = ws

    db.close()
    res = {weather_element: res}
    return res

# def  gen_answer(time, place, weather_element, res):
#     gen(self)


if __name__ == "__main__":
    res = query_place("西羊", limit=1)
    print(res)

    res = query_climate(180, 43, 109, "相对湿度")
    print(res)


