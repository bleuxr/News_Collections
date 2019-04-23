# ram_range=(1,1) 表示 unigram, ngram_range=(2,2) 表示 bigram, ngram_range=(3,3) 表示 thirgram
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
import jieba
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

# data = ["为了祖国，为了胜利，向我开炮！向我开炮！",
#         "记者：你怎么会说出那番话",
#         "我只是觉得，对准我自己打"]

data = [" ".join(jieba.lcut(e)) for e in data]         # 分词，并用" "连接
vector = CountVectorizer(min_df=1, ngram_range=(2,2))  # bigram
X = vector.fit_transform(data)                         # 将分词好的文本转换为矩阵
print(vector.vocabulary_ )                             # 得到特征
print(X)                                               #(句子下标, 单词特征下标)   频数
df1 = pd.DataFrame(X.toarray(), columns=vector.get_feature_names()) # to DataFrame
df1.head()