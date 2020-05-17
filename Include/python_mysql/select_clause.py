# or from mysql import connector
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="landy8530",
  database="test"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)


print("--------------------------------------------------------------")

mycursor.execute("SELECT name, address FROM customers")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)


# 如果您只对一行感兴趣，可以使用 fetchone() 方法。
#
# fetchone() 方法将返回结果的第一行：

print("--------------------------------------------------------------")

mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchone()

print(myresult)