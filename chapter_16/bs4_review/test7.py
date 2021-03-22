from datetime import datetime
import os

# 获取当前时间并格式化时间
time_now = datetime.now().strftime('%Y-%m-%d_%H%M%S')
# 获取当前目录
root_path = os.getcwd()
# 将当前目录与目标目录拼接并添加目录路径分隔符
path = os.path.join(root_path, f'{time_now}{os.sep}')
os.mkdir(path)
with open(f'{path}' 'test.txt', 'w', encoding='utf-8') as file:
    file.write('hello world')


from datetiem import datetime
  






















