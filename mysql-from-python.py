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
        rows = cursor.execute("DELETE FROM Friends WHERE name = 'bob';")
        connection.commit()
finally:
    # Close the connection, regardless of whether or not the above was
    # successful
    connection.close()
