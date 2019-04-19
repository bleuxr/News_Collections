import mysql.connector
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="2019my03sql31",
  database="toutiao"
)

mycursor=mydb.cursor()

mycursor.execute("SELECT id,title,abstract FROM fenci")

myresult=mycursor.fetchall()

corpus=[]
for x in myresult:

    id=x[0]
    title=x[1]
    abstract=x[2]

    corpus.append(title)

# corpus = ["110 万 房贷 贷款 30 年利率 4165 已经 年 提前 一部分 划得来 ", "天猫 创始 经理 告诉 下 一个 电商 风口 ", "手里 45 万 觉得 做点 生意 月 收入 万 以上 "]
vector = TfidfVectorizer()
tf_data = vector.fit_transform(corpus)
print(tf_data)    #(句子下标, 单词特征下标)   权重
print(vector.vocabulary_)    #单词特征
df1 = pd.DataFrame(tf_data.toarray(), columns=vector.get_feature_names()) # to DataFrame
df1