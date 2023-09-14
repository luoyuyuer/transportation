from datetime import datetime

datetime_format = "%Y-%m-%d %H:%M:%S"
start_datetime = datetime.strptime("2023-09-01 12:00:00", datetime_format)
end_datetime = datetime.strptime("2023-09-01 12:30:20", datetime_format)

delta = end_datetime - start_datetime
print(delta)  # 输出相差的时间差对象
