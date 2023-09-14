import pandas
from datetime import datetime
import bad_dispose

time_difference = []  # 存储两传感器之间的差值
keys = []  # 存储两传感器的标号，用于做获取的时间差值的key
time_dict = []  # 存储初步两两相减的时间结果


def create_time_dict(number):
    # 创建字典，列表为关键字，用来存储1月1日单辆汽车的数据
    if number == 1:
        return {f'list_{k}': [] for k in range(1, (len(bad_dispose.date_1_set) + 1))}
    if number == 2:
        return {f'list_{k}': [] for k in range(1, (len(bad_dispose.date_1_set) + 1))}


# 将获取的数据中的时间字符串解析为日期时间对象
def time_change(date_list):
    # 遍历字典列表，将时间字符串解析为日期时间对象
    for entry in date_list:
        entry['JGSJ'] = datetime.strptime(entry['JGSJ'], '%Y/%m/%d %H:%M:%S')


# 计算每辆车两个传感器之间的时间差值，并把超过5分钟的数值去除
def calculate_passing_time(list_dict):
    # 定义一个新的字典time_dict，第一个元素为车牌号，第二个元素key值为两个检测器标识，value为通过两个传感器所用的时间
    # 定义一个空列表，用来存放汽车通过两个传感器所用的时间的值
    global time_difference, time_dict
    for count_2 in range(1, (len(list_dict) + 1)):
        if len(list_dict[f"list_{count_2}"]) == 1:  # 假如汽车字典里只有一个时间，即字典里面的长度为1，则跳出循环，不进行相减
            continue
        for i in range(0, (len(list_dict[f'list_{count_2}']) - 1)):  # 从下标0到结束下标前一位进行遍历
            for j in range(i + 1, len(list_dict[f'list_{count_2}'])):  # 从下标1到结束下标进行遍历，保证每个元素都可相减
                time_difference.append(
                    list_dict[f'list_{count_2}'][j]['JGSJ'] - list_dict[f'list_{count_2}'][i]['JGSJ'])
                keys.append(list_dict[f'list_{count_2}'][j]['SSID'] + '-' + list_dict[f'list_{count_2}'][i]['SSID'])
        # 将key和value进行匹配，并在字典之前加上车牌号
        time_dict.append([list_dict[f"list_{count_2}"][0]['HPHM'], dict(zip(keys, time_difference))])
    return time_dict
# origin
#
# 柱状图、折线图、散点图
