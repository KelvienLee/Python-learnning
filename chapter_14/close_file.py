try:
    # 打开文件
    reader = open('test.txt', 'r', encoding='utf-8')
    # 操作文件
    content = reader.read()
    print(content)
except Exception:
    print(Exception)
finally:
    # 关闭文件
    reader.close()
