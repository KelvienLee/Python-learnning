# 一些其他函数
## isinstance()
### 判断数据类型的子类型是否为预期类型，返回布尔值
### isinstance(object, classinfo) ,classinfo 为必须
```python
a = 3.789
print(type(a))
print(isinstance(a, int))
```

## 查询 Python 内置函数
```python
>>> print(dir(__builtins__))
```
