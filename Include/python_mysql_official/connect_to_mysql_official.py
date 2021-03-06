import mysql.connector
from mysql.connector import errorcode

# refer to https://dev.mysql.com/doc/connector-python/en/connector-python-connectargs.html

config = {
    'user': 'root',
    'password': 'landy8530',
    'host': '127.0.0.1',
    'database': 'employees',
    'raise_on_warnings': True
}


def get_mysql_connect():
    try:
        cnx = mysql.connector.connect(**config)

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)

    return cnx
