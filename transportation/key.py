import configparser

# 创建配置文件解析器
config = configparser.ConfigParser()

# 读取配置文件
config.read('config.ini')

# 获取用户名和密码
host = config.get('Credentials', 'host')
port = int(config.get('Credentials', 'port'))
user = config.get('Credentials', 'user')
password = config.get('Credentials', 'password')
db = config.get('Credentials', 'db')


print(f'Username: {host}')
print(f'Password: {port}',type(port))
print(f'Username: {user}')
print(f'Password: {password}')
print(f'Username: {db}')


# import hashlib
#
# str = '123456'
#
# md5 = hashlib.md5()   				# 创建md5加密对象
# md5.update(str.encode('utf-8'))  	# 指定需要加密的字符串
# str_md5 = md5.hexdigest()  			# 加密后的字符串
#
# print(str_md5)						# 结果：e10adc3949ba59abbe56e057f20f883e