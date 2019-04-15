import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="2019my03sql31",
  database="toutiao"
)

mycursor=mydb.cursor()

mycursor.execute("SELECT id,title FROM information")

myresult=mycursor.fetchall()

for x in myresult:
  print(x[0]," ",x[1])
  break