import pymysql

class DBHelper:
    def __init__(self):
        self.con=pymysql.connect(host='localhost',port=3310,user='root',password='tiger',database='pythontest')
        query='create table if not exist user(userId int ,primary key, userName varchar(200),phone varchar(12))'
        cur=self.con.cursor()
        cur.execute(query)
        print("created")

helper=DBHelper()
