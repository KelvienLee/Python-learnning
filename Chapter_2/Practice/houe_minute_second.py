# 案例练习3 时分秒之间转换

seconds = int(input('请输入需要转换的秒数：'))
second = seconds % 60
minutes = seconds // 60
hour = minutes // 60
minute = minutes % 60
print('转换后为:', hour, '小时', minute, '分钟', second, '秒')
