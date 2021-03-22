import os

# # 查看目录和文件
# print(os.getcwd())     # 查看当前目录
# print(os.stat('handle_directory.py'))       # 获取指定路径的信息（文件或目录）
# print(os.path.abspath('zen.txt'))       # 获取当前路径的绝对路径
# print(os.path.getsize('zen.txt'))       # 获取文件大小（单位：字节）
# print(os.path.getctime('zen.txt'))      # 获取文件创建时间
# print(os.path.getatime('zen.txt'))      # 获取文件访问时间
# print(os.path.getmtime('zen.txt'))      # 获取文件修改时间

# 创建目录和文件
# os.mkdir('test1')       # 目录如果存在再次创建会报错
# os.mkdir('test1/test2')       # 在已经存在的目录下递归创建目录
# os.makedirs('python1/python2')      # 在不存在目录的情况下递归创建目录, 同样的，目录如果存在再次创建会报错
# 使用open()函数创建文件
# with open('test.py', 'w') as f:
#     pass
# 判断目录或文件是否存在
# if os.path.exists('test1/test2'):
#     print('文件已存在')
# else:
#     os.makedirs('test1/test2')

# 删除目录或文件
# os.rmdir('python1/python2')       #只能删除空文件夹
# os.removedirs('test1/test2')        # 可以递归删除，只能删除空文件夹，如果上级文件夹下有文件，则无法删除
# os.remove('python1/test1.py')       # 如果文件不存在则会报错


# 修改目录/文件
# os.mkdir('log.txt', mode=0o755)
# print(oct(os.stat('log.txt').st_mode))
# print(os.access('log.txt', os.R_OK))
# os.chmod('log.txt', 0o777)      # stat.S_I  更改权限
# print(os.stat('log.txt'))
# os.chown('log.txt', uid=2000, gid=3000)     # 更改用户组,根据实际情况填写
# os.rename('log.txt', 'log')         # 修改名称
# os.rename('log', 'python1/log')       # 修改名称的同时可以更改名字
# print(os.getcwd())
# os.chdir('python1/log')         # 修改目录
# print(os.getcwd())

# 判断是目录还是文件
# print(os.path.isfile('python1/python2/test2.py'))
# print(os.path.isdir('python1/python2/test2.py'))
#
# if os.path.isfile('python1/python2/test2.py'):
#     os.remove('python1/python2/test2.py')
# elif os.path.isdir('python1/python2/test2.py'):
#     os.rmdir('python1/python2/test2.py')
# else:
#     print('既不是文件也不是目录')


# 合并和分割目录
# path = os.getcwd()      # 获取当前目录
# filename = 'log.txt'
# # file_path = '\\'.join([path, filename])     # 字符串合并方式
# file_path = os.path.join(path, filename)        # os目录合并方式
# print(file_path)
#
# # 拆分目录
# print(os.path.split(file_path))         # 获取文件名及其目录
# print(os.path.splitext(file_path))      # 获取文件的后缀


# 遍历子目录
# path = os.getcwd()
# 遍历当前目录的一级内容
# print(os.listdir(path))

# 分层从根目录遍历所有层级内容
# walk_obj = os.walk(path)
# for num, item in enumerate(walk_obj):
#     print(f'第{num + 1}层：{item}')
