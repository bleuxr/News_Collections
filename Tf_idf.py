import mysql.connector
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
import pandas as pd

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

i=0
corpus=[]
for x in myresult:

    id=x[0]
    title=x[1]
    abstract=x[2]

    corpus.append(title)
    i=i+1
    if i>5:
      break

# corpus = ["110 万 房贷 贷款 30 年利率 4165 已经 年 提前 一部分 划得来 ", "天猫 创始 经理 告诉 下 一个 电商 风口 ", "手里 45 万 觉得 做点 生意 月 收入 万 以上 "]

# vector = TfidfVectorizer()
# tf_data = vector.fit_transform(corpus)
# print(tf_data)    #(句子下标, 单词特征下标)   权重
# print(vector.vocabulary_)    #单词特征
# df1 = pd.DataFrame(tf_data.toarray(), columns=vector.get_feature_names()) # to DataFrame
# df1


#将文本中的词语转换为词频矩阵
vectorizer = CountVectorizer()
#计算个词语出现的次数
X = vectorizer.fit_transform(corpus)
#获取词袋中所有文本关键词
word = vectorizer.get_feature_names()
print(word)
#查看词频结果
print(X.toarray())


# # 转化为TF矩阵
# cv = CountVect+orizer(tokenizer=lambda s: s.split())
# print(cv.get_feature_names())
# vectors = cv.fit_transform(corpus).toarray()
# print(vectors)

# # 求交集
# numerator = np.sum(np.min(vectors, axis=0))
# # 求并集
# denominator = np.sum(np.max(vectors, axis=0))
# # 计算杰卡德系数
# return 1.0 * numerator / denominator