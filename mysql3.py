import mysql.connector as connector
db= connector.connect(host='localhost',user='root',password='tiger',database='pythontest')
mycursor=db.cursor()
mycursor.execute("CREATE TABLE Person(name VARCHAR(50),age smallint UNSIGNED, personID int PRIMARY KEY AUTO INCREMENT)")
