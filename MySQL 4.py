import pymysql
try:
    query="create table employee(eno number, ename varchar(20),esal number(10,2),eaddr varchar2(10))"
    con=pymysql.connect('root/tiger@localhost')
    cursor=con.cursor()
    cursor.execute(query)
    print('Table created sucessfully')

except pymysql.DatabaseError as e:
    if con:
        con.rollback()
        print('There is a problem:',e)

finally:
    if cursor:
        cursor.close()

    if con:
        con.close()

