# or from mysql import connector
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="landy8530",
  database="test"
)

mycursor = mydb.cursor()


# 您可以使用 "DELETE FROM" 语句从已有的表中删除记录：
# 请注意语句 mydb.commit()。需要进行更改，否则表不会有任何改变。
sql = "DELETE FROM customers WHERE address = 'Mountain 21'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) deleted")


# 使用占位符 ％s 方法来转义值：防止 SQL 注入
sql = "DELETE FROM customers WHERE address = %s"
adr = ("Yellow Garden 2", )

mycursor.execute(sql, adr)

mydb.commit()

print(mycursor.rowcount, "record(s) deleted")