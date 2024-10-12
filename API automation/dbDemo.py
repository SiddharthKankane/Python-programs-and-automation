import mysql.connector
from utilities.configurations import *

#con = mysql.connector.connect(host='localhost', database='APIDevelop', user='root', password='Qrte654@zx')
con = getConnection()
print(con.is_connected())

cursor = con.cursor()
cursor.execute('select * from CustomerInfo')
row = cursor.fetchall()
print(row)

query = "Update CustomerInfo set Location =%s where CourseName = %s"
data = ("UK", "Jmeter",)

cursor.execute(query, data)
con.commit()

delete_query = "Delete from CustomerInfo where CourseName = %s "
data1 = ("WebServices", )
cursor.execute(delete_query, data1)
con.commit()

con.close()

if __name__ == '__main__':
    pass
