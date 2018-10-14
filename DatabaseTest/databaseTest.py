##import mysql.connector
import pymysql.cursors

connection = pymysql.connect(host='https://www.googleapis.com/sql/v1beta4/projects/csci-3030-team-3/instances/csci3030-team3',
                             user='python',
                             password='K56a44EEq2Hw',
                             db='TwitterBot',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
    # Read a single record
     sql = "SELECT * FROM `events`"
     #cursor.execute(sql, ('webmaster@python.org',))
     result = cursor.fetchone()
     print(result)
finally:
    connection.close()
    
##mydb = mysql.connector.connect(
##  host="35.196.238.195",
##  user="python",
##  passwd="K56a44EEq2Hw",
##  database="TwitterBot"
##)

##mycursor = mydb.cursor()

m##ycursor.execute("SELECT * FROM events ORDER by nextRunTime")

##myresult = mycursor.fetchall()

##for x in myresult:
##  print(x)
