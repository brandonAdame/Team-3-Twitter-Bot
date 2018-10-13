import mysql.connector

mydb = mysql.connector.connect(
  host="35.196.238.195",
  user="python",
  passwd="K56a44EEq2Hw",
  database="TwitterBot"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM events ORDER by nextRunTime")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
