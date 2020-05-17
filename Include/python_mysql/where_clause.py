# or from mysql import connector
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="landy8530",
  database="test"
)

mycursor = mydb.cursor()

sql = "SELECT * FROM customers WHERE address ='Park Lane 38'"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)


# 您也可以选择以给定字母或短语开头、包含或结束的记录。
#
# 请使用 ％ 表示通配符：

print("--------------------------------------------------------------")

sql = "SELECT * FROM customers WHERE address LIKE '%way%'"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)