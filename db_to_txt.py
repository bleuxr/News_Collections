import mysql.connector

import io
import sys
 
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="2019my03sql31",
  database="toutiao2"
)

mycursor=mydb.cursor()

mycursor.execute("SELECT id,abstract FROM information_news_tech LIMIT 0,1000")

myresult=mycursor.fetchall()

categories="科技"

i=0
for x in myresult:
  i=i+1
  #train
  # if i>0 and i<=800:
  #val
  # if i>800 and i<=900:
  #test
  if i>900 and i<=1000:
    if x[1] == "":
      continue
    print(categories+"   "+x[1])
