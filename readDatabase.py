import sqlite3

# establishing the connection
con = sqlite3.connect('TEST.db')
# preparing a cursor object
cursor = con.cursor()
# preparing sql statement
sql = '''
       SELECT * FROM EMPLOYEE
      '''
# executing the sql statement using `try ... except`
# noinspection PyBroadException
try:
    cursor.execute(sql)
except:
    print('Unable to fetch data.')

# fetching the records 

records = cursor.fetchall()

# Displaying the records

for record in records:
    print(record)

# closing the connection

con.close()
