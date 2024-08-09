import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user ='root',
    passwd = 'Amushree@1908'
    )

#prepare a curser objcect
cursorObject = dataBase.cursor()

#create theh database
cursorObject.execute("CREATE DATABASE mysqldb")

print("All Done!")
