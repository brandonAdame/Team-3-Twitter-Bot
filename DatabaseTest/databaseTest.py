import MySQLdb

conn = MySQLdb.connect(host="35.196.238.195", user="root", passwd="85v6EGGnz8FOmcgD", db="TwitterBot")
cursor = conn.cursor()

cursor.execute('SELECT * FROM events')
row = cursor.fetchone()

conn.close()

print(row)
