# 字符串格式化方法
# f-string
name = 'kelvien'
login_time = 10
cost = 458.69978
print(F'你好{name}，欢迎登录！ 这是你登录的第{login_time}次。 您本次消费{cost:.2f}元。恭喜{name}成为VIP!')
# ^|| 字符串前用符 f 或 F 来标注启用了 f-string 格式化的方法   {cost:.2f} 表示取小数点后2位

