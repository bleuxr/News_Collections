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

categories=["时尚","财经","游戏","体育","科技"]
querys=["fashion","finance","game","sport","tech"]

f_train = open('cnews/cnews.train.txt', 'w', encoding='utf-8')
f_test = open('cnews/cnews.test.txt', 'w', encoding='utf-8')
f_val = open('cnews/cnews.val.txt', 'w', encoding='utf-8')


for x in range(0,5):
  mycursor.execute("SELECT id,abstract FROM information_news_"+querys[x]+" LIMIT 0,10000")
  myresult=mycursor.fetchall()
  count=0
  for res in myresult:
    if res[1]=="":
      continue
    else:
      count=count+1
    print(count)
    # train 1000, test 200, val 100
    if count <= 1000:
      f_train.write(categories[x]+'\t'+res[1]+'\n')
    elif count <= 1200:
      f_test.write(categories[x]+'\t'+res[1]+'\n')
    elif count <= 1300:
      f_val.write(categories[x]+'\t'+res[1]+'\n')
    else:
      break


f_train.close()
f_test.close()
f_val.close()
