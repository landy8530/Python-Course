# or from mysql import connector
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="landy8530",
  database="test"
)

mycursor = mydb.cursor()

# 您可以使用 "UPDATE" 语句来更新表中的现有记录：
# 把地址列中的 "Valley 345" 覆盖为 "Canyoun 123"：
sql = "UPDATE customers SET address = 'Canyon 123' WHERE address = 'Valley 345'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) affected")

# mysql.connector 模块使用占位符 ％s 来转义 delete 语句中的值：
print("--------------------------------------------------------------")

sql = "UPDATE customers SET address = %s WHERE address = %s"
val = ("Valley 345", "Canyon 123")

mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record(s) affected")