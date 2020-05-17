# or from mysql import connector
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="landy8530",
  database="test"
)

mycursor = mydb.cursor()

# 结果排序
# 请使用 ORDER BY 语句按升序或降序对结果进行排序。
#
# ORDER BY 关键字默认按升序对结果进行排序。若要按降序对结果进行排序，请使用 DESC 关键字。


sql = "SELECT * FROM customers ORDER BY name"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)


print("--------------------------------------------------------------")

sql = "SELECT * FROM customers ORDER BY name DESC"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)