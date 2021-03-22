import time
from os import listdir
from tkinter import *           # 实际开发中并不提倡这种导入方法，因为这样可能造成与其他模块重名而出现Bug

start = time.perf_counter()

# 使用form...import...导入的模块使用时可以不声明模块名
print(listdir())

time.sleep(1)
end = time.perf_counter()
print(end - start)
