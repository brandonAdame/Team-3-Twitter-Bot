import mysql.connector

mydb = mysql.connector.connect(
  host="35.196.238.195",
  user="root",
  passwd="85v6EGGnz8FOmcgD",
  database="TwitterBot"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM events ORDER by nextRunTime")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
