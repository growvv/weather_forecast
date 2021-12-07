# weather_forecast

### 实现
1. 对问题进行实体识别

    - api: http://172.16.2.35:38868/api/recognize?question=我6月25号要去松山大桥，24号的大华岭隧道温度湿度怎么样？

    - 文档：https://documenter.getpostman.com/view/3868698/TzeZFnFd

2. 将数据导入到mysql数据库中
msp2_to_mysql.py

3. 从mysql中模糊查询数据
fuzzy_query.py

4. 模板生成得到回答
generate_answer.py

5. 对外提供api服务
fastapi_server.py

### 启动
1. 启动mysql服务
mysql -uroot -p

2. 启动fastapi服务
uvicorn main:app --reload
    - main：main.py文件
    - app：app = FastAPI() 在main.py内创建的对象。
    - --reload：在代码更改后重新启动服务器。 只有在开发时才使用这个参数。

还能查看自动生成的交互式API文档：http://127.0.0.1:8000/docs

