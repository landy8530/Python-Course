from __future__ import print_function
from datetime import date, datetime, timedelta

from connect_to_mysql_official import get_mysql_connect

cnx = get_mysql_connect()
cursor = cnx.cursor()

tomorrow = datetime.now().date() + timedelta(days=1)

add_employee = ("INSERT INTO employees "
                "(first_name, last_name, hire_date, gender, birth_date) "
                "VALUES (%s, %s, %s, %s, %s)")
add_salary = ("INSERT INTO salaries "
              "(emp_no, salary, from_date, to_date) "
              "VALUES (%(emp_no)s, %(salary)s, %(from_date)s, %(to_date)s)")

data_employee = ('Landy', 'Liu', tomorrow, 'M', date(1977, 6, 14))

# Insert new employee
"""
The information of the new employee is stored in the tuple data_employee. 
The query to insert the new employee is executed and we retrieve the newly inserted value for the emp_no column 
(an AUTO_INCREMENT column) using the lastrowid property of the cursor object.
"""
cursor.execute(add_employee, data_employee)
emp_no = cursor.lastrowid

# Insert salary information
data_salary = {
    'emp_no': emp_no,
    'salary': 50000,
    'from_date': tomorrow,
    'to_date': date(9999, 1, 1),
}
cursor.execute(add_salary, data_salary)

# Make sure data is committed to the database
cnx.commit()

cursor.close()
cnx.close()
