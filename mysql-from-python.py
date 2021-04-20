import os 
import datetime
import pymysql

username = os.getenv('VS_USER')

connection = pymysql.connect(host='localhost',
                             user=username,
                             password='',
                             db='Chinook')

try:
    # Run a query
    with connection.cursor(pymysql.cursors.DictCursor) as cursor:
        cursor.execute("""CREATE TABLE IF NOT EXISTS
                          Friends(name char(20), age int, DOB datetime);""")
finally:
    # Close the connection, regardless of whether or not the above was
    # successful
    connection.close()
