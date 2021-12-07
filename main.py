from typing import Optional

from requests.api import get

from fastapi import FastAPI
from pydantic import BaseModel
from fuzzy_query import query_place, query_climate
from return_answer import get_answer

app = FastAPI()

## 官方教程 https://fastapi.tiangolo.com/zh/
class Place_Item(BaseModel):
    name: str
    limit:  Optional[int] = 1

class Weather_Item(BaseModel):
    time: float
    lat: float
    lon: float
    weather_element: str

@app.get("/")
def read_root():
    return {"Hello": "World"}

# @app.post("/place")
# def q_palce(item: Place_Item):
#     res = query_place(place_name=item.name, limit=item.limit)
#     return res
#     # return {"time": item.time, "lat": item.lat, "lon": item.lon}

# @app.post("/weather")
# def q_weather(item: Weather_Item):
#     # return {"time": item.time, "lat": item.lat, "lon": item.lon}
#     print(item)
#     res = query_climate(time=item.time, lat=item.lat, lon=item.lon, weather_element=item.weather_element)
#     return res

@app.get("/question/")
def q_question(question: str = ""):
    answer = get_answer(question)

    return {"answer": answer}
    # return get_answer(question)
