import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="landy8530",
  database="test"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)

# 请注意语句 mydb.commit()。需要进行更改，否则表不会有任何改变。
mydb.commit()

print(mycursor.rowcount, "record inserted.")