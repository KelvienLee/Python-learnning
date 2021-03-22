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
