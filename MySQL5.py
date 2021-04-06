import pymysql
con = pymysql.connect('root/tiger@3310')
if con!= None:
    print('connection established sucessfully')
    print('Version:',con.version)
else:
    print('connection not established')

con.close()

