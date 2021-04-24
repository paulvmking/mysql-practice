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
    with connection.cursor() as cursor:
        cursor.execute("UPDATE Friends SET age = %s WHERE name = %s;",
                       (23, 'bob'))
        connection.commit()
finally:
    # Close the connection, regardless of whether or not the above was
    # successful
    connection.close()
