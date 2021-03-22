import time

# 获取时间戳
timestamp = time.time()
struct_time = time.localtime(timestamp)
year = struct_time.tm_year
month = struct_time.tm_mon
date = struct_time.tm_mday
print(year, month, date)

# 使用时间格式化的方法
timestamp = time.time()     # 获取时间戳
struct_time = time.localtime(timestamp)     # 从时间戳转化为当地世界
date_str = time.strftime('%Y-%m-%d', struct_time)      # 从sruct_time获取时间并转换格式  # 大写的Y是2021，小写的y是21
print(date_str)
result = date_str.split('-')
print(f'今天是{result[0]} {result[1]}月 {result[2]}日')
