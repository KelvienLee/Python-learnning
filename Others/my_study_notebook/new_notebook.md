# Python 学习笔记



## Chapter_8 函数基础

### 创建函数

* 函数命名应当使用小写字母加下划线的形式

  ```python
  def say_hi():
      print('hello world')
      print('welcome to weiguang19')
  
  
  say_hi()
  ```

### 使用函数的优点

1. 实现代码复用
2. 函数单一功能，便于管理和调用
3. 提高代码可读性

### 函数的参数

1. 普通参数
2. 默认参数
3. 关键字参数
4. 不定长参数

```python
# 函数的参数
# 普通参数
# 必须为每一个参数赋值，否则会报错
def window(width, height):
    print(f'window width:{width} \nwindow height: {height}')


# 普通参数按照顺序输出
window(25, 80)

# 定义参数(关键字参数）
window(height=18, width=9)


# 默认参数
def total(hour, salary=20):
    print(f'total salary of today: {hour*salary}')


# 定义了默认参数，在使用时如果不定义对应参数，会使用默认值，如果定义了参数则使用定义的参数
total(8)
total(12, 10)


# 关键字参数
def student(firstname, lastname):
    print(f'firstname is:{firstname}\nlastname is:{lastname}')


student('kelvin', 'Lee')


# 不定长参数
def my_function(height, age, *args, **kwargs):
    print(height)
    print(age)
    print(args)         # 将args输出为一个元组
    print(kwargs)       # 将kwargs输出为一个字典
    for arg in args:    # 遍历元组
        print(arg)
    for key, value in kwargs.items():       # 遍历字典
        print(f'{key}:{value}')


my_function(170, 18, 'hello', 'world', 'I', 'am', 'coming', lastname='kelvin', firstname='Lee')

```

### 函数的返回值

```python
# 函数的返回值
# 函数运行完成后返回的结果（值）
pi = 3.14


def area(r):
    return pi * (r ** 2)


print(area(2))


# 将分钟转换为时分
def minute_hour_exchange(input_minutes):
    hour = input_minutes // 60
    minute = input_minutes % 60
    return hour, minute


usr_input = int(input('input:'))
print(minute_hour_exchange(usr_input))                  # 返回元组
hours, minutes = minute_hour_exchange(usr_input)        # 将元组拆包
print(f'{usr_input}分钟是：{hours}小时 {minutes}分钟')
```



### 函数的作用域

```python
# 函数的作用域
# 全局变量
# 可变类型
a = 300
print(a)

# 不可变类型
b = [1, 2, 3]
print(b)


# 局部变量
def test1():
    a_fuc = 100
    print(a_fuc)
    # 对于不可变类型，需要使用global声明此操作可作用于全局
    global a
    a = 500
    # 对于可变类型，不需要任何声明也能作用于全局
    b.append(4)


test1()
print(a)
print(b)
```



### 函数的嵌套使用

```python
# 函数的嵌套
def get_up():
    print('睁开眼睛')
    print('穿衣服')
    print('洗脸')
    print('刷牙')


def breakfast():
    print('做早餐')
    print('吃早餐')


# 函数的内部嵌套调用
def to_work():
    get_up()
    breakfast()


to_work()


# 函数的内部嵌套定义编写
def test1():
    a = 10
    print('test1 starts execution.')
    print(f'test1 internal variable:{a}')

    def test2():
        nonlocal a
        a = 100
        print('test2 starts execution.')
        # 内部未定义变量的值会依次向外部寻找
        print(f'test2 internal variable:{a}')

    # 提示：使用了nonlocal函数便不能再使用global函数
    test2()
    print('test1 starts execution.')
    print(f'test1 internal variable:{a}')


test1()

```





## Chapter_13 异常处理
### 使用 try...except 处理异常
```python
# 使用 try...except处理异常
# 程序正常，执行try范围内的程序
try:
    age = int(input('请输入年龄：'))
    if age >= 18:
        print('你已成年')
    else:
        print('你未成年')

# 如果出现异常，执行except语句内的程序
except ValueError as error:
    print('输入不合法')
    print(error)

print('程序结束')
```

### 使用 try...except...else处理异常
```python
# 使用 try...except...else处理异常
try:                                      # 判断条件
    age = int(input('请输入年龄：'))

# 如果程序异常，执行except语句内的操作
except ValueError as error:
    print('输入不合法')

# 如果程序正常，执行else语句内的操作
else:
    if age >= 18:
        print('你已成年')
    else:
        print('你未成年')

print('程序结束')
```

### 使用try...except...finally 处理异常
```python
# 使用try...except...finally 处理异常

try:
    file = open('text.txt', 'w')
    s = 'hello world2.'
    file.write(s)

except:
    print('操作异常')

# 无论是否发生异常，都要执行的操作
finally:
    file.close()
    print('关闭文件')
```

### 处理多个异常
```python
# 处理多个异常
try:
    # 异常1: 用户输入是否正确
    age = int(input('请输入年龄:'))

    # 异常2: 运算是否有错误（0不能为除数）
    x = 10 / age

# 可以把错误写到一起
except (ValueError, ZeroDivisionError):
    print('请输入整数')

# 也可以把错误分开写
# except ZeroDivisionError:
#     print('年龄不能为0')
    
else:
    print(f'年龄是：{age}')
    print(f'x is {x}')

```

### 使用raise主动抛出异常
```python
# 使用raise主动抛出异常
age = int(input('请输入年龄:'))


def is_adult(age):
    if age < 18:
        raise Exception("你还未成年")
    

try:
    is_adult(age)
except ValueError as va:
    print(va)

print('continue')
```

### 自定义异常类
```python
# 自定义异常类

class ValidateError(ValueError):
    def __init__(self, message, *args, **kwargs):
        super().__init__(message, *args, **kwargs)


def validate_accout(username, password):
    if username == '':
        raise ValidateError('用户名不能为空')
    if password == '':
        raise ValidateError('密码不能为空')
    if username != 'kelvin' or password != '123456':
        raise ValidateError('用户名和密码不匹配')


username = input('请输入用户名：')
password = input('请输入密码：')
try:
    validate_accout(username, password)
except ValueError as va:
    print(va)
else:
    print('用户名和密码正确')
```

### 异常处理小结：
1. 将异常捕获做到最精确，不要一昧的使用大类。
2. 先捕获小异常，再捕获大异常。
3. 尽量使用Python标准库中的异常
4. 不要滥用异常
5. 使用异常会造成新性能损耗





## chapter_14 文件的操作



### 打开文件概述



```python
open (file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)

# file: 必需，文件路径（相对或者绝对路径）
# mode: 文件打开模式
# buffering: 设置缓冲
# encoding: 一般使用utf-8
# errors: 报错级别
# newline: 区分换行符
# closed: 设置打开底层文件描述符
# opener: 通过传递可调用的opener可以使用自定义开启器
```



#### 打开文件模式

> 基础模式：
>
> > w (write)
> >
> > r (read)
> >
> > x (xor)
> >
> > a (apend)

> 扩展模式（需配合基础模式使用）：
>
> > b (bytes)
> >
> > +(plus)

```python
# 打开文件
# r模式：当文件不存在时报错
# w模式：当文件不存在时会自动创建一个文件，覆盖源文件内容
# x模式：如果文件不存在就创建，如果存在就报错
# a模式：如果源文件中有内容，会追加到原文件后面
# b模式：不能单独使用，以二进制形式展示
# +模式：增强模式
file = open('zen.txt', 'a')
# 操作文件
# file.write('hello world.')
file.write('this is a test.')
# 关闭文件
file.close()
```



#### 操作文件指针的2种方法

```python
fileObject.tell()		# 获取文件指针当前位置
# 参数：无
# 返回值：文件指针当前位置
```

```python
fileObject.seek(offset[, whence])		# 用于移动文件读取指针到指定位置
# 参数
# - offset: 开始的偏移量，也就是代表需要移动偏移的字节数。
# - whecce: 可选，默认值为0.给offset一个定义，表示要从哪个位置开始偏移；
#     	    0代表文件开头开始算起，1代表从当前位置开始算起，2代表从文件末尾算起。
# 返回值
# 如果操作成功，则返回新的文件位置，如果操作失败，则函数返回-1.
```

```python
file = open('zen.txt', 'w+')

print(file.tell())
file.write('hello world.')
file.seek(6, 0)
print(file.tell())
content = file.read()
print(content)

file.close()
```



#### 写入文件的两种方法

> .write()		写入字符串
>
> .writelines()		写入字符串序列

```python
# 打开文件
file = open('test.txt', 'w', encoding='utf-8')

# 写入文件
# 写入字符串(write)
# file.write('hello \nworld')

# 写入字符串序列(writelines)
seq = ['人生苦短', '我用Python', 'hello', 'world']
file.writelines('\n'.join(seq))

# 关闭文件
file.close()
```



#### 读取文件的三种方法

> read()	读取全部，返回字符串
>
> readline()	读取一行，返回字符串
>
> readlines()	读取一行，返回列表

```python
# 打开文件
file = open('test.txt', 'r', encoding='utf-8')

# 操作文件
# read()方法
content = file.read()
print(content)


# readline()方法
# 一般不会使用这种方法：
line = file.readline()
print(line)             # hello\n
line = file.readline()
print(line)
line = file.readline()
print(line)
line = file.readline()
print(f'结束：{line}')

# 使用while语句依次读取：
line = file.readline()
while line != '':
    print(line, end='')
    line = file.readline()


# readlines()方法
# 返回列表
lines = file.readlines()
print(lines)

for line in lines:
    print(line, end='')

# 关闭文件
file.close()

```



#### 关闭文件

>  ❗️ 课程回顾：揭秘with语句



#### 查看目录或文件

```python
# 查看目录和文件
print(os.getcwd())     # 查看当前目录
print(os.stat('handle_directory.py'))       # 获取指定路径的信息（文件或目录）
print(os.path.abspath('zen.txt'))       # 获取当前路径的绝对路径
print(os.path.getsize('zen.txt'))       # 获取文件大小（单位：字节）
print(os.path.getctime('zen.txt'))      # 获取文件创建时间
print(os.path.getatime('zen.txt'))      # 获取文件访问时间
print(os.path.getmtime('zen.txt'))      # 获取文件修改时间
```



#### 创建目录或文件

```python
# 创建目录和文件
os.mkdir('test1')       # 目录如果存在再次创建会报错
os.mkdir('test1/test2')       # 在已经存在的目录下递归创建目录
os.makedirs('python1/python2')      # 在不存在目录的情况下递归创建目录,同样的，目录如果存在再次创建会报错
使用open()函数创建文件
with open('test.py', 'w') as f:
    pass
判断目录或文件是否存在
if os.path.exists('test1/test2'):
    print('文件已存在')
else:
    os.makedirs('test1/test2')
```



#### 删除目录或文件

```python
# 删除目录或文件
os.rmdir('python1/python2')       #只能删除空文件夹
os.removedirs('test1/test2')        # 可以递归删除，只能删除空文件夹，如果上级文件夹下有文件，则无法删除
os.remove('python1/test1.py')       # 如果文件不存在则会报错
```



#### 修改目录或文件（名字/权限）

```python
# 修改目录或文件（名字/权限）
os.mkdir('log.txt', mode=0o755)
print(oct(os.stat('log.txt').st_mode))
print(os.access('log.txt', os.R_OK))
os.chmod('log.txt', 0o777)      # stat.S_I  更改权限
print(os.stat('log.txt'))
os.chown('log.txt', uid=2000, gid=3000)     # 更改用户组,根据实际情况填写
os.rename('log.txt', 'log')         # 修改名称
os.rename('log', 'python1/log')       # 修改名称的同时可以更改名字
print(os.getcwd())
os.chdir('python1/log')         # 修改目录
print(os.getcwd())

```



#### 判断是文件还是目录

```python
# 判断是目录还是文件
print(os.path.isfile('python1/python2/test2.py'))
print(os.path.isdir('python1/python2/test2.py'))

if os.path.isfile('python1/python2/test2.py'):
    os.remove('python1/python2/test2.py')
elif os.path.isdir('python1/python2/test2.py'):
    os.rmdir('python1/python2/test2.py')
else:
    print('既不是文件也不是目录')
```



#### 合并和分割目录

```python
# 合并和分割目录
path = os.getcwd()      # 获取当前目录
filename = 'log.txt'
# file_path = '\\'.join([path, filename])     # 字符串合并方式
file_path = os.path.join(path, filename)        # os目录合并方式
print(file_path)

# 拆分目录
print(os.path.split(file_path))         # 获取文件名及其目录
print(os.path.splitext(file_path))      # 获取文件的后缀
```



#### 遍历子目录

```python
# 遍历子目录
path = os.getcwd()
# 遍历当前目录的一级内容
print(os.listdir(path))

# 分层从根目录遍历所有层级内容
walk_obj = os.walk(path)
for num, item in enumerate(walk_obj):
    print(f'第{num + 1}层：{item}')
```





## chapter 15 MySQL 操作

### connection 连接对象

#### connection 对象方法

> cursor()				获取游标对象，操作数据库
>
> commit()			  提交事务
>
> rollback()           回滚事务
>
> close()				  关闭数据库连接

### Python 操作数据库基本流程

```python
import pymysql

try:
    connect = pymysql.connect(
        host='localhost',
        user='root',
        password='*********',
        db='shop',
        charset='utf8'
    )
except Exception as e:
    print(e)

try:
    # 获取游标对象
    with connect.cursor() as cursor:
        # SQL语句
        sql = """
        create table test(
        id int auto_increment primary key,
        name varchar(255) not null
        );
        """
        # 执行SQL语句
        cursor.execute(sql)
        # 提交操作
        connect.commit()
        # 获取数据
        # result = cursor.fetchone()
        # print(result)

except Exception as e:
    print(e)

finally:
    # 关闭数据库连接
    connect.close()


```

### Python 操作MySQL -- 增改删

```python
import pymysql

try:
    connect = pymysql.connect(
        host='localhost',
        user='root',
        password='WGX9.mysql',
        db='shop',
        charset='utf8'
    )
except Exception as e:
    print(e)

try:
    # 如果要批量操作 a
    # data = [(0, '小米11', '3800', '小米手机', 1, '2021-01-30'),
    #         (0, 'OPPO', '4800', '欧珀手机', 1, '2021-02-15'),
    #         (0, 'VIVO', '2800', '维蜗手机', 1, '2021-03-30')]
    # 获取游标对象
    with connect.cursor() as cursor:
        # SQL语句
        # sql_update = 'update goods set description = "维沃手机" where id = 14'
        sql_delete = 'delete from goods where id = 8'

        # 如果要批量操作 b
        # sql_create = """
        # insert into goods values(%s, %s, %s, %s, %s, %s)
        # """

        # 执行SQL语句
        # cursor.execute(sql_update)
        cursor.execute(sql_delete)

        # 如果要批量操作 c
        # cursor.executemany(sql_create, data)

        # 提交操作
        connect.commit()

except Exception as e:
    print(e)

finally:
    # 关闭数据库连接
    connect.close()

```

### Python 操作My3SQL -- 查询

```python
import pymysql

try:
    connect = pymysql.connect(
        host='localhost',
        user='root',
        password='WGX9.mysql',
        db='shop',
        charset='utf8',
        cursorclass=pymysql.cursors.DictCursor          # 设置为字典游标
    )
except Exception as e:
    print(e)

try:
    # 获取游标对象
    with connect.cursor() as cursor:
        # SQL语句
        # 设置筛选条件
        sql_select = 'select * from goods where price > 4000'
        # 不设置筛选条件
        # sql_select = 'select * from goods'

        # 执行SQL语句
        cursor.execute(sql_select)

        # 查找数据
        # 只获取一条数据
        # result = cursor.fetchone()
        # 获取多条数据
        # result = cursor.fetchmany(3)
        # 获取所有数据
        result = cursor.fetchall()


except Exception as e:
    print(e)

finally:
    # 关闭数据库连接
    connect.close()

print(result)
# 只打印一条数据
# print(f'商品名称：{result["name"]}， 价格：{result["price"]}')

# 打印多条数据
for goods in result:
    print(f'商品名称：{goods["name"]}， 价格：{goods["price"]}')

```



## chapter_16 网络爬虫基础

### requests 模块

#### requests 模块请求方法

| 方法    | 描述                                                        |
| ------- | ----------------------------------------------------------- |
| GET     | 请求页面，并返回页面内容                                    |
| HEAD    | 类似get请求，只不过返回的响应中没有具体的内容，用于获取报头 |
| POST    | 大多用于提交表单或上传文件，数据包含在请求中                |
| PUT     | 从客户端向服务器传送的数据取代指定文档中的内容              |
| DELETE  | 请求服务器删除指定的页面                                    |
| CONNECT | 把服务器当作跳板，让服务器代替客户端访问其他网页            |
| OPTIONS | 允许客户端查看服务器的性能                                  |
| TRACE   | 回显服务器受到的请求，主要用于测试或诊断                    |

```python
import requests

url = 'https://httpbin.org/get'
response = requests.get(url)
print(response)

```

#### 模块请求参数

```python
import requests

url = 'https://httpbin.org/post'
username = input('username:')
password = input('password:')
age = input('age:')
payload = {
    'username': username,
    'password': password,
    'age': age
}

# get请求带参数
# response = requests.get(url, params=payload)

# post请求带参数,数据不会被显示在网址中
response = requests.post(url, data=payload)
print(response)
print(response.url)

```



#### 添加请求头

```python
# 添加请求头
headers = {
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
}
response = requests.get(url, headers=headers)
print(response)
print(response.url)

```

#### 伪造请求头

```python
# 伪造请求头
ua = UserAgent(verify_ssl=False)
user_agent = ua.random
headers = {
    'User-Agent': user_agent
}
response = requests.get(url, headers=headers)
print(response)
print(response.url)

```

### BeautifulSoup4 模块基础

#### 常用解析器

| 解析器          | 使用方法                             | 优势                                                         | 劣势                       |
| --------------- | ------------------------------------ | ------------------------------------------------------------ | -------------------------- |
| Python标准库    | BeautifulSoup(markup, "html.parser") | Python内置标准库  <br />速度适中  <br />文档容错能力强       | 老旧版本中文档容错能力差   |
| lxml HTML解析器 | "lxml"                               | 速度快<br />文档容错能力强                                   | 需安装C语言库              |
| lxml XML 解析器 | "xml"                                | 速度快<br />唯一支持XML的解析器                              | 需安装C语言库              |
| html5lib        | "html5lib"                           | 最好的容错性<br />以浏览器的方式解析文档<br />生成HTML格式的文档 | 速度慢<br />不依赖外部扩展 |

#### 四大对象

```python
from bs4 import BeautifulSoup
import requests
import lxml

url = 'http://8.135.6.248/'
try:
    response = requests.get(url)
except RuntimeError:
    print('请求失败')


html_content = response.text

# BeautifulSoup类型  获取整个html文档
soup = BeautifulSoup(html_content, 'xml')
print(type(soup))

# Tag类型  获取html标签
print(soup.title)
print(type(soup.title))

# NavigableString类型，获取标签内容
print(soup.title.string)
print(type(soup.title.string))

# 只能获取到匹配到的第一个标签
print(soup.a)
# 标签下还有嵌套标签的话无法获取字符串内容
print(soup.a.string)             # 返回None

# Comment类型 获取html中的注释
```

#### 常用操作

```python
# 获取页面em标签, 获取兄弟节点
print(soup.em)
# 获取文档原始内容（如空格等不显示的内容）
print(repr(soup.em.next_sibling))
print(soup.em.next_sibling.next_sibling)

# 获取em标签的父节点
print(soup.em.parent.parent.parent)
print(soup.em.parents)      # 返回生成器
for item in soup.em.parents:
    print(item)
    print()
```

> find语法
>
> find(name, attrs, recursive, string, **kwargs)
>
> > - name 参数可以查找所有名为name的tag，字符串对象会被自动忽略。
> > - attrs 搜索时会把该参数当作指定名字tag的属性来搜索
> > - recursive 检索当前tag的所有子孙节点
> > - string 搜索字符串

```python
# find方法
nav = soup.find('ul', {'class': 'top-nav-right'})
# print(nav)
for item in nav.children:
    # print(repr(item))
    if item != '\n':
        print(item.span.string)

# find_all方法
nav = soup.find_all('div', {'class': 'top-nav-items'})
for item in nav:
    if item.span:
        print(item.span.string)

# select方法
nav = soup.select('.top-nav-items .login-event')
for item in nav:
    print(item.span.string)

```

n