from __future__ import print_function

from decimal import Decimal
from datetime import datetime, date, timedelta

from connect_to_mysql_official import get_mysql_connect

# Connect with the MySQL Server
cnx = get_mysql_connect()

"""
To iterate through the selected employees, we use buffered cursors. 
(A buffered cursor fetches and buffers the rows of a result set after executing a query; 
see Section 10.6.1, “cursor.MySQLCursorBuffered Class”.) 
This way, it is unnecessary to fetch the rows in a new variables. Instead, the cursor can be used as an iterator.
"""

# Get two buffered cursors
curA = cnx.cursor(buffered=True)
curB = cnx.cursor(buffered=True)

# Query to get employees who joined in a period defined by two dates
query = (
    "SELECT s.emp_no, salary, from_date, to_date FROM employees AS e "
    "LEFT JOIN salaries AS s USING (emp_no) "
    "WHERE to_date = DATE('9999-01-01')"
    "AND e.hire_date BETWEEN DATE(%s) AND DATE(%s)")

# UPDATE and INSERT statements for the old and new salary
update_old_salary = (
    "UPDATE salaries SET to_date = %s "
    "WHERE emp_no = %s AND from_date = %s")
insert_new_salary = (
    "INSERT INTO salaries (emp_no, from_date, to_date, salary) "
    "VALUES (%s, %s, %s, %s)")

# Select the employees getting a raise
curA.execute(query, (date(2000, 1, 1), date(2000, 12, 31)))

tomorrow = datetime.now().date() + timedelta(days=1)

# Iterate through the result of curA
for (emp_no, salary, from_date, to_date) in curA:
    # Update the old and insert the new salary
    new_salary = int(round(salary * Decimal('1.15')))
    print("emp_no:" + str(emp_no), "old_salary:" + str(salary), "new_salary:" + str(new_salary))
    curB.execute(update_old_salary, (tomorrow, emp_no, from_date))
    curB.execute(insert_new_salary,
                 (emp_no, tomorrow, date(9999, 1, 1, ), new_salary))

    # Commit the changes
    cnx.commit()

cnx.close()
