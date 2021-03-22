# # 打开文件常用模式
#
# # r模式，当文件不存在时会报错
# file = open('zen.txt', 'r')
#
# # w模式，文件不存在时自动创建文件,写入的内容会覆盖原文件内容
# file_w = open('zen.txt', 'w')
#
# # x模式,如果文件不存在则创建，如果文件存在则报错
# file_x = open('zen.txt', 'x')
#
# # a模式，如果原文件有内容，会将内容追加在原文件之后
# file_a = open('zen.txt', 'a')
#
# # b模式,不能单独使用，必须结合基础模式，读取和写入二进制文件
# # wb，写入二进制文件
# file_wb = open('zen_b.txt', 'wb')
# file_wb.write(bytes('hello world', encoding='utf-8'))
#
# # rb，读取二进制文件
# file_rb = open('zen_b.txt', 'rb')
# content = file_rb.read()
# print(content)
#
# # plus模式,增强模式
# # 可读可写
# file_rp = open('zen_b.txt', 'r+')
# # 可写可读
# file_wp = open('zen_b.txt', 'w+')
# # 可追加写入也可读
# file_ap = open('zen_b.txt', 'a+')


# 文件指针






























