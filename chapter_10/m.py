# 从包（文件夹）中导入模块（自定义模块）
from package1 import module1
from package2 import module3

print(dir(module1))
print(module1.__name__)
print(module3.__package__)
