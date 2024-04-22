import mysql.connector as mc
from mysql.connector import Error


try:
    connection = mc.connect(host='localhost',
                                         database='drone_dispatch',
                                         user='root',
                                         password='') #enter your password
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
