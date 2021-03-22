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









