import pymysql

try:
    connect = pymysql.connect(
        host='localhost',
        user='root',
        password='WGX9.mysql',
        db='shop',
        charset='utf8'
    )
    print(connect)
except Exception as e:
    print(e)

print(dir(connect))
