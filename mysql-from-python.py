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
        rows = [(23, 'bob'),
                (24, 'jim'),
                (25, 'fred')]
        cursor.executemany("UPDATE Friends SET age = %s WHERE name = %s;",
                           rows)
        connection.commit()
finally:
    # Close the connection, regardless of whether or not the above was
    # successful
    connection.close()
