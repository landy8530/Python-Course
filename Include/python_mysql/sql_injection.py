# or from mysql import connector
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="landy8530",
  database="test"
)

mycursor = mydb.cursor()
# 防止 SQL 注入
# 此举是为了防止 SQL 注入，这是一种常见的网络黑客技术，可以破坏或滥用您的数据库。
# 使用占位符 ％s 方法来转义查询值：

sql = "SELECT * FROM customers WHERE address = %s"
adr = ("Yellow Garden 2", )

mycursor.execute(sql, adr)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
