# 在同一目录下的自定义模块可以直接导入
import my_function
from my_function import subtraction
import sys      # 查找模块目录函数

# 导入不在同一目录下的自定义模块
import utils.function_branch

print(sys.path)

add = my_function.add(8, 9)
print(add)

subtraction = subtraction(10, 3)
print(subtraction)

# 但是在使用其他目录导入的函数的时候，也要用带目录的全名
multiplication = utils.function_branch.multiplication(8, 9)
print(multiplication)


# 也可以这样导入
# 如果该模块中的内容不是函数，则直接输出该模块中内容
from Chapter_1 import hello