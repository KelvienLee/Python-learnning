from openpyxl import Workbook
from openpyxl.styles import Font

# 实例化模块
wb = Workbook()
# 激活工作表
ws = wb.active

# 写入表头
sheet_title = ['姓名', '性别', '年龄']
ws.append(sheet_title)

# 可以使用列表，也可使用元组
rows = (
    ('kelvin', '男', '18'),
    ('jack', '男', '20'),
    ('张三', '男', '34')
)
for row in rows:
    ws.append(row)


wb.save('test1.xlsx')
