from gensim.models import Word2Vec                  
import numpy as np
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="2019my03sql31",
  database="toutiao"
)

mycursor=mydb.cursor()

mycursor.execute("SELECT id,title,abstract FROM fenci")

myresult=mycursor.fetchall()

data=[]
for x in myresult:

    id=x[0]
    title=x[1]
    abstract=x[2]

    data.append(title)

# data = ["I love deep learning","I love studying","I want to travel"]
#词频少于min_count次数的单词会被丢弃掉
#size指特征向量的维度为50
#workers参数控制训练的并行数
train_w2v = Word2Vec(data,min_count=5,size=50, workers=4)
avg_data=[]
for row in data:         #计算平均词向量，表示句子向量
    vec = np.zeros(50)
    count = 0
    for word in row:
        try:
            vec += train_w2v[word]
            count += 1
        except:
            pass
    avg_data.append(vec/count)  
print(avg_data[1])