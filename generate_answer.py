import os

en2cn = dict()
en2cn['precipitations'] = '降水量'
en2cn['relative_humidity'] = '相对湿度'
en2cn['temperature'] = '温度'
en2cn['u_component_of_wind'] = 'u风'
en2cn['v_component_of_wind'] = 'v风'
unit = dict()
unit['precipitations'] = 'mm'
unit['relative_humidity'] = '%'
unit['temperature'] = 'C'
unit['u_component_of_wind'] = 'm/s'
unit['v_component_of_wind'] = 'm/s'


def answer_template_init(template_dir_path, template_filename_list=None):
    """
    回答模板初始化
    从回答模板文件夹中的文件读取回答，存储到 answer_template 变量中，并返回。
    """
    answer_template = []
    if template_filename_list is None:
        qa_template_files = os.listdir(template_dir_path)
    else:
        qa_template_files = template_filename_list
    for t_file in qa_template_files:

        t_file_path = os.path.join(template_dir_path, t_file)
        with open(t_file_path, 'r', encoding='utf-8') as f:
            content = f.readlines()
        line_list = list(map(lambda i: i.strip(), content))
        for line in line_list:
            if line != '':
                answer_template.append(line)
    return answer_template


def generate_answer(data_dict, answer_template, answer_index=0):
    """
    填写回答模板
    :param data_dict: 输入数据（用户、天气、事件）
    :type data_dict: dict
    :param answer_template: 回答模板
    :type answer_template: list
    :param answer_index: 选中的回答模板的index，目前模板只有一个，默认为0，后期根据方法获取
    :type answer_index: int
    """
    strip = ","

    # 获取模板
    template = answer_template[answer_index]
    # 将数据填充进入模板
    if len(data_dict['weather']) > 1:
        weather_idx = 0
        for i in range(len(data_dict['weather']) - 1):
            left = template[:-1]
            right = template[-1]
            expend_line = strip + '{weather' + str(i + 1) + '}为{result' + str(i + 1) + '}'
            template = left + expend_line + right
        time = data_dict['time']
        location = data_dict['location']
        template = template.replace('{time}', str(time))
        template = template.replace('{location}', str(location))
        for weather in data_dict['weather']:
            if weather_idx == 0:
                template = template.replace('{weather}', str(en2cn[weather]))
                template = template.replace('{result}', str(data_dict['weather'][weather]) + unit[weather])
            else:
                temp_weather = '{weather' + str(weather_idx) + '}'
                temp_result = '{result' + str(weather_idx) + '}'
                template = template.replace(temp_weather, str(en2cn[weather]))
                template = template.replace(temp_result, str(data_dict['weather'][weather]) + unit[weather])
            weather_idx += 1
    else:
        time = data_dict['time']
        location = data_dict['location']
        template = template.replace('{time}', str(time))
        template = template.replace('{location}', str(location))
        template = template.replace('{weather}', str(en2cn[list(data_dict['weather'].keys())[0]]))
        template = template.replace('{result}', str(list(data_dict['weather'].values())[0]) + unit[
            list(data_dict['weather'].keys())[0]])

    return template


if __name__ == '__main__':
    data={'time':"2021年6月19日",'weather':{'precipitations':1,'relative_humidity':2,'temperature':3,'u_component_of_wind':4,'v_component_of_wind':5},'location':"棋盘梁隧道东侧"}
    rtn = answer_template_init('template')
    print(generate_answer(data, rtn))