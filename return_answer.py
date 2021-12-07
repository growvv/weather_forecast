from IPython.terminal.ipapp import IPAppCrashHandler
from requests.api import get
from generate_answer import generate_answer, answer_template_init
from fuzzy_query import query_weather
import requests
import json
import ipdb

def get_answer(query):
    if query == "":
        return "Please enter a query."
    
    # 通过params传参
    query_params = {'question': query}
    response = requests.get(url='http://172.16.2.35:38868/api/recognize/', params = query_params)
    if response.status_code != 200:
        return "Error: " + response.status_code
    else:
        data =  json.loads(response.text)['data']['result']
        # location = data['location'][0]
        # timestamp = data['timestamp'][0]
        # weather_element = data['weather'][0]

        location_mock = '武汉大学'
        timestamp_mock = '2019-01-01'
        weather_element_mock = '温度'


        res = query_weather(location_mock, timestamp_mock, weather_element_mock)
        # ipdb.set_trace()
        data={'time':timestamp_mock,'weather':{'precipitations':1,'relative_humidity':2,'temperature':res['temperature'],'u_component_of_wind':4,'v_component_of_wind':5},'location':"棋盘梁隧道东侧"}

        rtn = answer_template_init('template')
        print(data)
        rtn = generate_answer(data, rtn)
        # ipdb.set_trace()
        return rtn


if __name__ == '__main__':
    query = '我6月25号要去松山大桥，24号的大华岭隧道温度湿度怎么样？'
    print(get_answer(query))