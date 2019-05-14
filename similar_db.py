from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
from scipy.linalg import norm
import mysql.connector

np.set_printoptions(threshold=np.inf)

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="2019my03sql31",
  database="toutiao"
)

mycursor=mydb.cursor()

mycursor.execute("SELECT id,title,abstract FROM fenci")

myresult=mycursor.fetchall()

datanum=100
i=0
data=[]
for x in myresult:

    id=x[0]
    title=x[1]
    abstract=x[2]

    # data.append(title)
    data.append(title)
    i=i+1
    if i>=datanum:
      break
 
def tf_similarity(s1, s2):

    # def add_space(s):
    #     return ' '.join(list(s))
    # # 将字中间加入空格
    # s1, s2 = add_space(s1), add_space(s2)

    # 转化为TF矩阵
    cv = CountVectorizer(tokenizer=lambda s: s.split())
    corpus = [s1, s2]
    vectors = cv.fit_transform(corpus).toarray()
    # print(vectors)
    # 计算TF系数
    return np.dot(vectors[0], vectors[1]) / (norm(vectors[0]) * norm(vectors[1]))
 
 
# s1 = '你在干嘛呢'
# s2 = '你在干什么呢'
# print(tf_similarity(s1, s2))

result=np.zeros([1000,1000])

for x in range(0,datanum):
    for y in range (0,datanum):
        if x==y:
            continue
        res=tf_similarity(data[x],data[y])
        if res>0.4:
            print(data[x])
            print(data[y])
            result[x][y]=res
            print(x," ",y," ",res)

#打印相似度二维数组
# print("    ",end='')
# for i in range(0,datanum):
#   print("%6d"%(i),end='')
# print()
# for x in range(0,datanum):
#     print("%4d "%(x),end='')
#     for y in range (0,datanum):
#         print("%5.2f "%(result[x][y]),end='')
#     print()
