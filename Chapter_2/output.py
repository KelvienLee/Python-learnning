# 最简单的输出
print('# 简单的直接输出')
print('hello world')
print('hello python',end='\n\n')

# 输出变量
print('# 输出变量')
price = 10
number = 6
print(price,number)
print('单价',price,'元每个')
print('购买数量',number,'个')
print('总共需付',price*number,'元',end='\n\n')                   # 变量之间可以相互运算

# 使用sep分隔符
# 用sep定义输出语句之间的连接符
print('# 使用sep分隔符')
print('this', 'is', 'a', 'test')
print('this', 'is', 'a', 'test',sep=' ')                        # sep='空格'时，无显示效果
print('hello','world','hello','python',sep=',')
print('1949','10','01',sep='-')                                 # 可用于时间格式显示
print('lixingqiang06','gmail.com',sep='@',end='\n\n')           # 可用于邮箱格式书写

# end结束符
# end=''之后就不能再继续使用逗号添加内容了，否则就会出错
print('# end结束符')
print('hello',end=',')                                          # end结束符的下一行会与此行一起显示
print('world')
print('lixingqiang06',end='@')                                  # end结束符也可以定义为具体的符号，但不常用。
print('gmail.com')
print('this','is',end='\n\n')                                   # 一个 \n 结束符只换行不隔行，要隔行至少需要两个换行符号
print('a','test',end='\n\n')


# file 输出文件
# 有待学习，可不用理解。
print('# file 输出文件')
file_source = open('test.txt','w')
print('hello python.',file=file_source)
file_source.close()