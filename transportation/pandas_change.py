import pandas as pd
import link
import time
from tqdm import tqdm
import numpy

# 程序运行开始时间
start_time = time.time()
number_11 = 0

# 使表完全显示
pd.set_option('display.max_columns', 100000)
pd.set_option('display.width', 100000)
pd.set_option('display.max_colwidth', 100000)
pd.set_option("display.max_rows", None)

# 读取date_1_list、date_1_list，下文进行格式转化
nested_dict_list_1 = link.date_1_list
nested_dict_list_2 = link.date_2_list

# 存储根据条件筛选出需要删除的行
rows_to_delete = []

# 转为 DataFrame
df1 = pd.DataFrame(nested_dict_list_1)
df2 = pd.DataFrame(nested_dict_list_2)


# 新增列名，以存储结束路段的数据，以及结束路段与开始路段的时间差
def add_columns(df):
    df.insert(loc=2, column='ID_CD', value=df['SSID'] + '-' + df['CDBH'])
    df = df.drop(columns=['HPZL', 'SSID', 'CDBH'])

    df.columns = [f'{col}_{i + 1}' for i, col in enumerate(df.columns)]

    df = df.assign(ID_CD_4=pd.Series(), JGSJ_5=pd.Series(),
                   time=pd.Series(), total_time=pd.Series(), 备注=pd.Series())
    return df


df1 = add_columns(df1)
df2 = add_columns(df2)

counts_1 = df1['ID_CD_2'].value_counts()
counts_2 = df2['ID_CD_2'].value_counts()
print(counts_1, counts_2)

#
def time_split(df):
    # 将时间戳分箱为小时段
    bins = pd.date_range(start=df['JGSJ_3'].min(), end=df['JGSJ_3'].max(), freq='15T')
    df['hour_bin'] = pd.cut(df['JGSJ_3'], bins=bins)

    # 统计每个小时段内的数据量
    minutely_counts = df['hour_bin'].value_counts().reset_index()

    # 重命名列
    minutely_counts.columns = ['Minutes Range', 'Count']

    # 输出结果
    print(minutely_counts)


time_split(df1)
time_split(df2)


# 剔除数据、增加数据条件
def del_data(condition):
    global rows_to_delete, df
    # 根据条件筛选出需要删除的行
    rows_to_delete = df[condition]
    # 使用 drop 方法删除这些行
    df = df.drop(rows_to_delete.index)
    # 重置索引
    df = df.reset_index(drop=True)
#
#
# # 剔除完全不进入车道的数据
# condition1 = (df['ID_CD_2'].isin(['HK-92-6', 'HK-93-1', 'HK-93-5', 'HK-93-6', 'HK-93-10', 'HK-93-11']))
# # 根据条件筛选出需要删除的行
# del_data(condition1)
#
# # 输出单个数据
# condition2 = ((df['HPHM_1'] != df.shift(1)['HPHM_1']) & (df['HPHM_1'] != df.shift(-1)['HPHM_1']))
# # 根据条件筛选出需要删除的行,这里把单个数据进行删除
# del_data(condition2)
#
# # 判断单行数据跟下一行车牌号是否一致
# condition3 = (df['HPHM_1'] == df.shift(-1)['HPHM_1'])
# # HK-92可进入实际路段,部分情况要考虑'HK-92-8', 'HK-92-9', 'HK-92-10'
# condition4 = (df['ID_CD_2'].isin(['HK-92-7', 'HK-92-8', 'HK-92-9', 'HK-92-10']))
# # HK-93可进入实际路段,部分情况要考虑'HK-93-3', 'HK-93-4', 'HK-93-12'
# condition5 = (df['ID_CD_2'].isin(['HK-93-2', 'HK-93-3', 'HK-93-4', 'HK-93-12']))
# # HK-92监测到的下一个路段的传感器数据
# condition6 = (df['ID_CD_2'].isin(['HK-107-3', 'HK-107-4', 'HK-93-7', 'HK-93-8', 'HK-93-9']))
# # HK-93监测到的下一个路段的传感器数据
# condition7 = (df['ID_CD_2'].isin(['HK-107-1', 'HK-107-2', 'HK-93-7', 'HK-93-8', 'HK-93-9']))
# # 中间路段的传感器
# condition8 = (df['ID_CD_2'].isin(['HK-107-1', 'HK-107-2']))
# condition9 = (df['ID_CD_2'].isin(['HK-107-3', 'HK-107-4']))
# # 结束路段的传感器
# condition10 = (df['ID_CD_2'].isin(['HK-92-1', 'HK-92-2', 'HK-92-3', 'HK-107-3', 'HK-107-4']))
# condition11 = (df['ID_CD_2'].isin(['HK-93-7', 'HK-93-8', 'HK-93-9']))
#
# for i in tqdm(range(1, len(df['HPHM_1']))):
#     if condition3.iloc[i - 1] & condition4.iloc[i - 1] & condition6.iloc[i]:
#         df.at[i - 1, 'ID_CD_4'] = df.at[i, 'ID_CD_2']
#         df.at[i - 1, 'JGSJ_5'] = df.at[i, 'JGSJ_3']
#     elif condition3.iloc[i - 1] & condition5.iloc[i - 1] & condition7.iloc[i]:
#         df.at[i - 1, 'ID_CD_4'] = df.at[i, 'ID_CD_2']
#         df.at[i - 1, 'JGSJ_5'] = df.at[i, 'JGSJ_3']
#     elif condition3.iloc[i - 1] & condition8.iloc[i - 1] & condition10.iloc[i]:
#         df.at[i - 1, 'ID_CD_4'] = df.at[i, 'ID_CD_2']
#         df.at[i - 1, 'JGSJ_5'] = df.at[i, 'JGSJ_3']
#     elif condition3.iloc[i - 1] & condition9.iloc[i - 1] & condition11.iloc[i]:
#         df.at[i - 1, 'ID_CD_4'] = df.at[i, 'ID_CD_2']
#         df.at[i - 1, 'JGSJ_5'] = df.at[i, 'JGSJ_3']
# pass
# condition13 = df['ID_CD_4'].isna()
# del_data(condition13)
#
# condition14 = (df['HPHM_1'] == df.shift(-1)['HPHM_1'])
# condition15 = (df['ID_CD_2'].isin(['HK-93-12']))
# condition16 = (df['ID_CD_4'].isin(['HK-107-1', 'HK-107-2']))
#
# condition17 = (df['total_time']) > pd.Timedelta(minutes=30)
#
# for i in range(1, (len(df) + 1)):
#     df.at[i - 1, 'time'] = df.at[i - 1, 'JGSJ_5'] - df.at[i - 1, 'JGSJ_3']
#     if df['time'].iloc[i - 1] > pd.Timedelta(minutes=30):
#         if condition15.iloc[i - 1] & condition16.iloc[i - 1]:
#             df.at[i - 1, '备注'] = '时间过长，极有可能中途回小区'
#             number_11 += 1
#     if df['time'].iloc[i - 1] > pd.Timedelta(minutes=30):
#         print(df.iloc[i - 1])
# # 判断单行数据跟上一行车牌号是否一致
# condition12 = (df['HPHM_1'] == df.shift(-1)['HPHM_1'])
#
# j = 0
# df.at[j, 'total_time'] = df['time'].iloc[0]
# for i in range(1, (len(df))):
#     if condition12.iloc[i - 1]:
#         df.at[j, 'total_time'] = df['total_time'].iloc[j] + df['time'].iloc[i]
#     else:
#         j = i
#         df.at[j, 'total_time'] = df['time'].iloc[j]
#
# end_time = time.time()
# # print(df)
#
# execution_time = end_time - start_time
# print(f"代码执行时间: {execution_time} 秒,{number_11}")

# condition3 = (df['HPHM_1'] == df.shift(-1)['HPHM_1'])
# # # 进一步判断可进入车道但也可不进入车道的车辆是否进入
# condition6 = (
#     df['ID_CD_2'].isin(['HK-92-7', 'HK-92-8', 'HK-92-9', 'HK-92-10', 'HK-93-2', 'HK-93-3', 'HK-93-4', 'HK-93-12']))
# condition10 = (df['ID_CD_2'].isin(['HK-107-1', 'HK-107-2', 'HK-107-3', 'HK-107-4']))
# condition7 = (df['ID_CD_2'].isin(['HK-92-1', 'HK-92-2', 'HK-92-3',
#                                   # 'HK-107-1', 'HK-107-2', 'HK-107-3', 'HK-107-4',
#                                   'HK-93-7', 'HK-93-8', 'HK-93-9']))
#
# x = 0
# a = []
# a1 = []
#
# for i in tqdm(range(2, len(df))):
#     if condition3.iloc[i - 2]:
#         if condition6.iloc[i - 2]:
#             if condition10.iloc[i - 1]:
#                 if condition7.iloc[i] and condition3.iloc[i - 1]:
#                     # df1.loc[len(df1)] = df.loc[i-1]
#                     # df1.loc[len(df1)] = df.loc[i - 1]
#                     # df1.loc[len(df1)] = df.loc[i]
#                     a.append(df.iloc[i-2,0])
#                     a1.append(df.iloc[i,2]-df.iloc[i-2,2])
#                     x += 1
#                     continue
#                 else:
#                     # df1.loc[len(df1)] = df.loc[i - 2]
#                     # df1.loc[len(df1)] = df.loc[i - 1]
#                     a.append(df.iloc[i - 2, 0])
#                     a1.append(df.iloc[i-1, 2] - df.iloc[i - 2, 2])
#                     x += 1
#                     continue
#             else:
#                 if condition7.iloc[i - 1]:
#                     # df1.loc[len(df1)] = df.loc[i - 2]
#                     # df1.loc[len(df1)] = df.loc[i - 1]
#                     a.append(df.iloc[i - 2, 0])
#                     a1.append(df.iloc[i-1, 2] - df.iloc[i - 2, 2])
#                     x += 1
#                     continue
#         else:
#             if condition10.iloc[i - 2] and condition7.iloc[i - 1]:
#                 # df1.loc[len(df1)] = df.loc[i - 2]
#                 # df1.loc[len(df1)] = df.loc[i - 1]
#                 a.append(df.iloc[i - 2, 0])
#                 a1.append(df.iloc[i-1, 2] - df.iloc[i - 2, 2])
#                 x += 1
#                 continue
#     else:
#         continue
# pass
# df1 = pd.DataFrame(columns=['id', 'time'])
# L=dict(zip(a, a1))
# # L = pd.DataFrame(L)
# print(L)
