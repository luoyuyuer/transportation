import pandas as pd
import link
import bad_dispose_1

pd.set_option('display.max_columns', 100000)
pd.set_option('display.width', 100000)
pd.set_option('display.max_colwidth', 100000)
# 显示所有行
pd.set_option("display.max_rows", None)
nested_dict_list = link.date_1_list

rows_to_delete = []

# 转为 DataFrame
df = pd.DataFrame(nested_dict_list)

df.insert(loc=2, column='ID_CD', value=df['SSID'] + '-' + df['CDBH'])
df = df.drop(columns=['HPZL', 'SSID', 'CDBH'])

df.columns = [f'{col}_{i + 1}' for i, col in enumerate(df.columns)]

df = df.assign(ID_CD_4=pd.Series(), JGSJ_5=pd.Series(),
               ID_CD_6=pd.Series(), JGSJ_7=pd.Series(), time=pd.Series())


# 剔除数据、增加数据条件
def del_data(condition):
    global rows_to_delete, df
    # 根据条件筛选出需要删除的行
    rows_to_delete = df[condition]
    # 使用 drop 方法删除这些行
    df = df.drop(rows_to_delete.index)
    # 重置索引
    df = df.reset_index(drop=True)


# 剔除完全不进入车道的数据
condition1 = (df['ID_CD_2'].isin(['HK-92-6', 'HK-93-1', 'HK-93-5', 'HK-93-6', 'HK-93-10', 'HK-93-11']))
del_data(condition1)

# 输出单个数据
condition2 = ((df['HPHM_1'] != df.shift(1)['HPHM_1']) & (df['HPHM_1'] != df.shift(-1)['HPHM_1']))
# 根据条件筛选出需要删除的行
del_data(condition2)


# 判断单行数据跟下一行车牌号是否一致
condition3 = (df['HPHM_1'] == df.shift(1)['HPHM_1'])
# 进一步判断可进入车道但也可不进入车道的车辆是否进入
# 识别这些车道
condition4 = (df['JGSJ_3'].isin(['HK-92-8', 'HK-92-9', 'HK-92-10', 'HK-93-3', 'HK-93-4', 'HK-93-12']))
# 识别这些车道的出口
condition5 = (df['JGSJ_3'].isin(['HK-92-1', 'HK-92-2', 'HK-92-3',
                                 'HK-107-1', 'HK-107-2', 'HK-107-3', 'HK-107-4',
                                 'HK-93-7', 'HK-93-8', 'HK-93-9']))
# 判断与上个数据车牌是否一致
condition6 = (df['HPHM_1'] == df.shift(-1)['HPHM_1'])
#
condition7 = (df['ID_CD_2'].isin(['HK-93-1', 'HK-93-2', 'HK-93-3', 'HK-93-4', 'HK-93-12']))

# # 根据条件筛选出需要删除的行
# rows_to_delete = df[condition2]
# # 使用 drop 方法删除这些行
# df = df.drop(rows_to_delete.index)
# # 重置索引
# df = df.reset_index(drop=True)
#
# # 根据条件筛选出需要删除的行
# rows_to_delete = df[condition1]
# # 使用 drop 方法删除这些行
# df = df.drop(rows_to_delete.index)
# # 重置索引
# df = df.reset_index(drop=True)


# for i in range(1, (len(df['HPHM_1']) + 1)):
#     if condition6.iloc[i - 1]:
#         df.at[i - 1, 'ID_CD_4'] = df.at[i, 'ID_CD_2']
#         df.at[i - 1, 'JGSJ_5'] = df.at[i, 'JGSJ_3']
#
# # 删除ID_CD_4为空的行
# df = df.dropna(subset=['ID_CD_4'], axis=0)
#
# # 重置索引
# df = df.reset_index(drop=True)
#
# condition2 = (df['HPHM_1'] == df.shift(1)['HPHM_1'])
#
# for i in range(1, len(df['HPHM_1'])):
#     if condition2.iloc[i]:
#         df.at[i - 1, 'ID_CD_6'] = df.at[i, 'ID_CD_4']
#         df.at[i - 1, 'JGSJ_7'] = df.at[i, 'JGSJ_5']
#     elif condition7.iloc[i]:
#         continue
#     else:
#         df.at[i, 'time'] = df.at[i, 'JGSJ_5'] - df.at[i, 'JGSJ_3']
#


print(df)
