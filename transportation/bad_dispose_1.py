import link
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

num = 0  # 用于统计车辆被监测数据次数
count = 1
count_1 = 1

date_1_set = set()  # 存1号车辆的集合
date_2_set = set()  # 存2号车辆的集合

car1_count_list = []  # 存放1号每辆车辆被监测数据次数
car2_count_list = []  # 存放2号每辆车辆被监测数据次数
data1_value = []  # 存放1号车辆被监测数据次数的总数（相同次数为1种）
data2_value = []  # 存放2号车辆被监测数据次数的总数
categories = []  # 存放柱状图x轴数据


# 检查字典中是否存在特定的键，并将其对应的值添加到集合中
def car_set(car_list, number):
    for i in car_list:
        if number == 1:
            date_1_set.add(i['HPHM'])
        elif number == 2:
            date_2_set.add(i['HPHM'])


# 创建两个列表，用于保存一个列表仅存一种车辆
def create_list_dict(number):
    # 创建字典，列表为关键字，用来存储1月1日单辆汽车的数据
    if number == 1:
        return {f'list_{k}': [] for k in range(1, (len(date_1_set) + 1))}
    if number == 2:
        return {f'list_{k}': [] for k in range(1, (len(date_2_set) + 1))}


# 例如，初始化一个长度为len(list_1_dict)的列表，用来存放汽车被监测次数的数据
def create_list(number):
    """
    :param number:用来区别第一天跟第二天的数据
    :return: 返回空列表，长度与汽车集合相同
    """
    if number == 1:
        global car1_count_list
        n = len(create_list_dict(1))
        car1_count_list = [0] * n
    if number == 2:
        global car2_count_list
        n = len(create_list_dict(2))
        car2_count_list = [0] * n


# 得到单一列表仅存一种车辆
def car_count(date_set, date_list, number):
    """
    :param date_set: 汽车集合
    :param date_list: 某一天的汽车所有被监测的数据列表
    :param number: 用来区别第一天跟第二天的数据
    :return: 数据经过升序排列且经过剔除之后的数据列表，每辆车被监测次数，监测次数的总数
    """
    global count, count_1, num  # 声明 count 为全局变量
    list_1_dict = create_list_dict(1)
    list_2_dict = create_list_dict(2)
    create_list(1)
    create_list(2)
    for j in date_set:  # 先对车辆集合进行遍历
        for i in date_list:  # 对车辆列表进行遍历
            if i["HPHM"] == j:  # 车辆列表的车牌号跟车辆集合相同，则将数据取出存于list_{i}_dict中
                # date_1_list.append(i)
                if number == 1:
                    list_1_dict[f'list_{count}'].append(i)
                elif number == 2:
                    list_2_dict[f'list_{count}'].append(i)
                num += 1  # 进入if次数多少则说明被监测的数据的次数
        if number == 1:
            car1_count_list[count - 1] = num  # 将被监测的数据次数依此存于其中
        elif number == 2:
            car2_count_list[count - 1] = num
        # 剔除一些被监测到但未进入该车道
        """
        HK-92:CDBH=6,8,9
        HK-107
        HK-93:CDBH=1,3,5,6,10
        """
        # 将监测到一次数据且不驶入车道内部的车辆数据进行剔除，将数据设置为空
        if num == 1:
            if number == 1:
                if (list_1_dict[f'list_{count}'][0]['SSID'] == 'HK-93') and (
                        list_1_dict[f'list_{count}'][0]['CDBH'] == 1 or 3 or 5 or 6 or 10 or 11) or (
                        list_1_dict[f'list_{count}'][0]['SSID'] == 'HK-92') and (
                        list_1_dict[f'list_{count}'][0]['CDBH'] == 6 or 8):
                    list_1_dict[f'list_{count}'] = []
                    count -= 1
            elif number == 2:
                if (list_2_dict[f'list_{count}'][0]['SSID'] == 'HK-93') and (
                        list_2_dict[f'list_{count}'][0]['CDBH'] == 1 or 3 or 5 or 6 or 10 or 11) or (
                        list_2_dict[f'list_{count}'][0]['SSID'] == 'HK-92') and (
                        list_2_dict[f'list_{count}'][0]['CDBH'] == 6 or 8):
                    list_2_dict[f'list_{count}'] = []
                    count -= 1
        count += 1
        num = 0
    count = 1
    # 使用字典推导式过滤掉值为空的项，即去掉监测到一个数据但并不进行车道驶入的数据
    list_1_dict = {k: v for k, v in list_1_dict.items() if v != []}
    list_2_dict = {k: v for k, v in list_2_dict.items() if v != []}
    # 获取最大被监测次数，依此将每辆车被监测次数数据插入data_value里
    if number == 1:
        for i in range(1, (max(car1_count_list) + 1)):
            data1_value.insert(i - 1, car1_count_list.count(i))
        # for i in range(1, len(list_1_dict) + 1):
        #     list_1_dict[f'list_{i}'] = sorted(list_1_dict[f'list_{i}'], key=lambda x: x['JGSJ'], reverse=False)
        return list_1_dict, car1_count_list, data1_value
    if number == 2:
        for i in range(1, (max(car2_count_list) + 1)):
            data2_value.append(car2_count_list.count(i))
        # 对时间进行升序排列
        # for i in range(1, (len(date_2_set) + 1)):
        #     list_2_dict[f'list_{i}'] = sorted(list_2_dict[f'list_{i}'], key=lambda x: x['JGSJ'], reverse=False)
        # print(list_2_dict)
        return list_2_dict, car2_count_list, data2_value


def draw_hist(number):
    """
    :param number:绘制哪一天的柱状图
    :return:
    """
    # 获取第一天的汽车数据
    global data1_value, categories
    print(data1_value)  # 打印被监测次数的总数
    for i in range(1, (len(data1_value) + 1)):  # 创建x轴
        categories.append(f"{i}")
    print(categories)  # 打印x轴数据
    # 绘制柱状图
    plt.rcParams['font.sans-serif'] = ['SimSun']
    plt.hist(categories, bins=16)  # 分成16个区间
    # x,y,主标题，字体为宋体
    plt.xlabel('汽车被采集到的数据次数', fontproperties='SimHei')
    plt.ylabel('数据次数的总数', fontproperties='SimHei')
    plt.title('汽车采集被数据次数分类', fontproperties='SimHei')
    # 将x轴与y轴的数据长度进行匹配
    for i in range(0, (len(categories))):
        plt.bar(categories[i], data1_value[i])
    plt.show()


if __name__ == '__main__':
    car_set(link.date_1_list, 1)
    car_set(link.date_2_list, 2)
    print(date_1_set, len(date_1_set))  # 8935
    print(date_2_set, len(date_2_set))  # 8987
