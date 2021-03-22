# 打开文件
# r模式：当文件不存在时报错
# w模式：当文件不存在时会自动创建一个文件，覆盖源文件内容
# x模式：如果文件不存在就创建，如果存在就报错
# a模式：如果源文件中有内容，会追加到原文件后面
# b模式：不能单独使用，以二进制形式展示
# +模式：增强模式
file = open('zen.txt', 'a')
# 操作文件
# file.write('hello world.')
file.write('this is a test.')
# 关闭文件
file.close()
