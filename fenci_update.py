import jieba
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="2019my03sql31",
  database="toutiao"
)

mycursor=mydb.cursor()

mycursor.execute("SELECT id,abstract FROM information")

myresult=mycursor.fetchall()

for x in myresult:

    id=x[0]

    seg_list = jieba.cut(x[1], cut_all=False)
    #print("Default Mode: " + "/".join(seg_list))  # 精确模式
    abstract="/".join(seg_list)
    
    sql="UPDATE fenci SET abstract = %s WHERE id = %s"
    val=(abstract,id)
    mycursor.execute(sql,val)
    
mydb.commit()