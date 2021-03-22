# import time     # 使用import 直接导入整个模块，在调用模块方法的时候要声明模块名称
# import os
from time import perf_counter, sleep            # 使用from方法导入的模块在使用时可以不用声明模块而直接使用
from os import *                            # 使用*号表示导入该模块下的所有方法,使用时需要声明模块    在实际应用中一般不适用此种方法

start = perf_counter()
sleep(1)
print(listdir())
end = perf_counter()
print(end - start)

