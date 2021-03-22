import openpyxl

# 导入excel
wb = openpyxl.load_workbook('test.xlsx')

# 选择worksheet
print(wb.sheetnames)
ws = wb['用户信息']
print(ws)
ws_index = wb.sheetnames
ws2 = wb[ws_index[1]]
print(ws2)


# 获取数据
ws1 = wb['用户信息']
result = ws1['A1'].value
print(result)

# 获取每一行数据
for row in ws1.rows:
    data = [cell.value for cell in row]
    print(data)

# 获取行数和列数
print(ws1.max_row)
print(ws1.max_column)
# 迭代行
for row in ws1.iter_rows(min_row=2, min_col=1, max_row=ws1.max_row, max_col=ws1.max_column):
    # print(row)
    data = [cell.value for cell in row]
    print(data)

print('\n\n')

# 迭代列
for column in ws1.iter_cols(min_row=2, min_col=1, max_row=ws1.max_row, max_col=ws1.max_column):
    # print(column)
    data = [cell.value for cell in column]
    print(data)


# 关闭表格
wb.close()
