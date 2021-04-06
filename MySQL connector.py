import pymysql
mydb=pymysql.connect(host="localhost",
                             user="root",
                             password="tiger",
                             database="mydatabase")
mycursor=mydb.cursor()
#mycursor.execute("CREATE DATABASE mydatabase")
mycursor.execute("SHOW DATABASE")
for x in mycursor:
    print(x)