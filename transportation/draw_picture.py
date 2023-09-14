
# # 扇形图
# import matplotlib.pyplot as plt
#
# plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体
# plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题
#
# # for i in range(1, 8):
# #     exec(f'num_{i} = i')
#
# # 数据
# labels = ['监测到一次时间次数',
#           '监测到两次时间次数',
#           '监测到三次时间次数',
#           '监测到四次时间次数',
#           '监测到五次时间次数',
#           '监测到六次时间次数',
#           '监测到七次时间次数',
#           '监测到八次时间次数']
#
# sizes = [25, 30, 15, 30]
#
# # 颜色
# colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
#
# # 绘制扇形图
# plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
#
# # 指定图表的标题
# plt.title("汽车被监测到的时间次数")
#
# # 显示图表
# plt.show()
