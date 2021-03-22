# with open('test.txt', 'r', encoding='utf-8') as reader:
#     content = reader.read()
#     print(content)


# class FileManager(object):
#     def __init__(self, name, mode):
#         print('调用__init__方法')
#         self.name = name
#         self.mode = mode
#         self.file = None
#
#     def __enter__(self):
#         print('调用__enter__方法')
#         self.file = (self.name, self.mode)
#         return self.file
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print('调用__exit__方法')
#         if self.file:
#             self.file.close()
#
#
# with FileManager('test.txt', 'r') as file:
#     print('准备读取文件')
#     content = file.read()
#     print(content)











