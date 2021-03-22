import os

# 查看目录和文件
# 查看当前目录
# cwd = os.getcwd()
# print(cwd)
# # 获取指定路径信息(可以是文件或目录）
# stat = os.stat('handle_directory.py')
# print(stat)
# abspath = os.path.abspath('test.txt')
# # 获取文件的绝对路径
# print(abspath)
# # 获取文件大小
# getsize = os.path.getsize('test.txt')
# print(getsize)
# # 获取文件创建时间(时间戳）
# getctime = os.path.getctime('test.txt')
# print(getctime)
# # 访问时间
# os.path.getatime('test.txt')
# # 修改时间
# os.path.getmtime('test.txt')

# # 创建目录
# # mkdir()
# # mkdir只能创建一个文件夹，不能递归创建，文件夹已存在则报错
# os.mkdir('test1')
# # test1 已经存在，在其下创建子文件夹不会报错
# os.mkdir('test1/test2')
# # # python1 不存在，不能直接递归创建文件夹
# os.mkdir('python1/python2')
#
# # # os.makedirs()
# # # 可以递归创建文件,如果文件夹已存在，同样会报错
# os.makedirs('python1/python2')
#
#
# # # open()创建空文件
# with open('test_file.txt', 'w') as file:
#     pass
#
#
# # # 判断文件或文件夹是否存在
# if os.path.exists('test1/test2'):
#     print('File exists')
# else:
#     os.makedirs('test1/test2')


# 删除目录和文件
# os.rmdir()
# 删除空目录,文件夹不为空则报错
# os.rmdir('python1')
# # 可以递归式删除，目标目录为空则可以成功删除
# os.rmdir('test1/test2')
#
# # os.removedirs()
# # 递归删除空文件夹，不为空则报错，如果上层文件夹存在文件则无法删除
# os.removedirs('test1/test2')
#
# # os.remove()
# # 删除文件，文件不存在则报错
# os.remove('test_file.txt')


# # 修改目录和文件
# # 可以在创建目录时为其设置权限
# os.mkdir('log.txt', mode=0o755)
#
# # 使用函数命令更改权限
# os.chmod('log.txt', 0o777)
# print(os.stat('log.txt').st_mode)
#
# # 更改用户组(根据实际情况填写）
# # os.chown('log.txt', uid=, gid=)
#
# # 重命名文件或文件夹
# os.rename('test.txt', 'text_rename.txt')
# os.rename('log.txt', 'log')
# # 可以和移动文件同时执行
# os.rename('test1.txt', 'log/tes1.txt')
# os.rename('text_rename.txt', 'log/test.txt')


# # 判断目录和文件
# is_file = os.path.isfile('./log/test.txt')
# is_dir = os.path.isdir('./log/test.txt')
# print(is_file)
# print(is_dir)
# if os.path.isfile('./log/test.txt'):
#     os.remove('./log/test.txt')
# else:
#     print('这不是一个文件')


# 合并和分割目录
# path = os.getcwd()
# file_name = 'log.txt'
#
# # 字符串拼接方法
# # file_path = '/'.join([path, file_name])
# # 合并目录
# file_path = os.path.join(path, file_name)
#
# # 分割目录
# # 获取文件绝对目录和文件名
# print(os.path.split(file_path))
# # 获取文件绝对目录、文件名、后缀
# print(os.path.splitext(file_path))


# 遍历子目录
# path = os.getcwd()
# # print(os.listdir(path))
# walk_obj = os.walk(path)
# for num, item in enumerate(walk_obj):
#     print(f'第{num+1}层:{item}')

for i, j in enumerate(range(20)):
    i += 1
    j += 3
    print(i)
    print(j)

