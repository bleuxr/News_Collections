import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="2019my03sql31",
  database="toutiao"
)

mycursor=mydb.cursor()
#mycursor.execute("CREATE TABLE fenci (id VARCHAR(25) not null, title VARCHAR(255) not null)")

sql="INSERT INTO fenci (id,title) VALUES(%s,%s)"
val=("6640600094619992324","test")
mycursor.execute(sql,val)

mydb.commit()

print(mycursor.rowcount,"record inserted.")