import pymysql
def Connect():
    c = pymysql.connect(
        host='localhost',
        user='root',
        password='Priyansha21',
        database='python_july'
    )
    return c

#conn = Connect()
#cr =conn.cursor()
##cr.execute(q)
#result = cr.fetchall() #1.returns single first data  2.fetchall returns all the data values 3.fetchmany returns specific values
##for i in result:
   # print(i) #2 sepearte tuples




