import mysql.connector
dataBase=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='root'
)

cursorObject=dataBase.cursor()

cursorObject.execute("CREATE DATABASE nemoco")
print("DONE !! ! ☆*: .｡. o(≧▽≦)o .｡.:*☆")