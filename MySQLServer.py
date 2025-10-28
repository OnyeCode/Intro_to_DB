import mysql.connector

mydb = mysql.connector.connect(
        host = 'localhost',
        username = 'root',
        password = '**********',
        database = 'test_db'
        )

mycursor = mydb.cursor()

try:
    mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
except mysql.connector.Error as e:
    print(e)
else:
    print("Database 'alx_book_store' created successfully!")
finally:
    mycursor.close()
    mydb.close()
