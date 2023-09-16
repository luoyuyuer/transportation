# 数据连接
from pymysql import Connection, cursors
# import sqlalchemy
# import time_translation
import key
conn = Connection(
        host=key.host,
        port=key.port,
        user=key.user,
        password=key.password,
        db=key.db,
)

cursor = conn.cursor(cursors.DictCursor)  # 将导出的数据库数据改为列表-字典格式
# cursor = conn.cursor()
cursor.execute('select * from sjcj_t_clxx_ls')  # 选择sjcj_t_clxx_ls文件
# cursor.execute("delete from sjcj_t_clxx_ls where HPHM = '车牌'")  # 删除所有未识别出来的车牌
date_list = cursor.fetchall()  # 将所有数据存于date_list中
print(date_list)

# sql语句，选择出2019年1月1日的车辆 "SELECT * FROM sjcj_t_clxx_ls WHERE JGSJ LIKE '%2019-01-01%'"
cursor.execute("SELECT * FROM sjcj_t_clxx_ls WHERE JGSJ LIKE '%2019-01-01%'")  # 对全部数据进行划分，分为1号监测和2号监测
date_1_list = cursor.fetchall()  # 将1号数据存于date_1_list中
# time_translation.time_change(date_1_list)   # 对获取的时间字符串数据进行格式更改

# sql语句，选择出2019年1月2日的车辆 "SELECT * FROM sjcj_t_clxx_ls WHERE JGSJ LIKE '%2019-01-02%'"
cursor.execute("SELECT * FROM sjcj_t_clxx_ls WHERE JGSJ LIKE '%2019-01-02%'")  # 选择2号数据
date_2_list = cursor.fetchall()

# 关闭游标
cursor.close()

# 数据库关闭
conn.close()


if __name__ == '__main__':
    print(conn.get_server_info())  # 获取安装的mysql的版本号，验证连接正确性
    print(date_1_list, type(date_1_list))  # 展示1月1日数据，以及数据类型
    print(date_2_list, type(date_2_list))  # 展示1月2日数据，以及数据类型
    print(len(date_1_list), len(date_2_list))
    # print(dt, type(date_1_list[0]['JGSJ']))
    try:
        if (len(date_1_list) + len(date_2_list)) == len(date_list):
            print(
                f"数据传输初步无误，第一天有{len(date_1_list)}个数据，第二天有{len(date_2_list)}个数据，等于整合的{len(date_list)}个数据")
    except Exception as e:
        print("数据区分有错误")
