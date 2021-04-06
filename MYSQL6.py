import pymysql
try:
    #query=INSERT INTO EMPLOYEE(ENO,ENAME,ESAL,EADDR) VALUES(100,'durga',1000,'hyd')
    con= pymysql.connect(host='localhost',database='pythontest',user='root',password='tiger')
    cursor = con.cursor()
    query="insert into employees values(100,'rutuja',1000,'pune')"
    #cursor=con.cursor()
    cursor.execute(query)
    con.commit()
    print('Record inserted successfully')
except pymysql.DatabaseError as e:
    if con:
        con.rollback()
        print('There is a problem:',e)
finally:
    if cursor:
        cursor.close()

    if con:
        con.close()



