# import sqlalchemy
import pandas
import bad_dispose_1
import link
import time_translation

# import draw_picture

# 得到一天时间内车的集合，参数1为一天传感器获得的全部数据，参数2为调用的次数
bad_dispose_1.car_set(link.date_1_list, 1)
bad_dispose_1.car_set(link.date_2_list, 2)
# print(bad_dispose.date_1_set, len(bad_dispose.date_1_set))  # 8935
# print(bad_dispose.date_2_set, len(bad_dispose.date_2_set))  #8987
# print(link.date_2_list, len(link.date_2_list))

# 得到单一列表仅存一种车辆
list_1_dict, car1_count_list, data1_value = bad_dispose_1.car_count(bad_dispose_1.date_1_set, link.date_1_list, 1)
list_2_dict, car2_count_list, data2_value = bad_dispose_1.car_count(bad_dispose_1.date_2_set, link.date_2_list, 2)
print(list_1_dict, len(list_1_dict), type(list_1_dict['list_1'][0]["JGSJ"]))
print(data1_value, len(data1_value))
# print(list_1_dict['list_8935'][0]['CDBH'],type(list_1_dict['list_8935'][0]['CDBH']))
# print(list_1_dict)

# bad_dispose_1.draw_hist(1)
# print(list_1_dict)
# time_translation.calculate_passing_time(list_1_dict)
# print(data1_value, data2_value)
# print(bad_dispose.draw_hi warnings.warn("loaded more than 1 DLL from .libs:"st(1))
#

# time = time_translation.calculate_passing_time(list_1_dict)
# print(time, type(time))

# 剔除一个时间数据的车辆

# # 关闭数据库连接
# link.conn.close()
