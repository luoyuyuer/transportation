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

if __name__ == '__main__':
    print(f'Username: {host}')
    print(f'Password: {port}', type(port))
    print(f'Username: {user}')
    print(f'Password: {password}')
    print(f'Username: {db}')
