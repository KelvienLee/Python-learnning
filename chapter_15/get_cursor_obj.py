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









