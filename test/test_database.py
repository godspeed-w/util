import  pymysql

# 打开数据库连接
config = {
          'host':'127.0.0.1',
          'port':3306,
          'user':'root',
          'password':'12345678',
          'database':'springboot',
          'charset':'utf8'
          }
db = pymysql.connect(**config)

# 使用 cursor() 方法创建一个游标对象
cursor = db.cursor()

# 使用 execute()  方法执行 SQL 查询 
cursor.execute("select * from user")

# 使用 fetchone() 或者fetchall() 方法获取数据
data = cursor.fetchall()
print(data)

# 关闭数据库连接
db.close()