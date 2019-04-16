import re
import jieba
import mysql.connector

## 去除停用词的2个函数
# 创建停用词list
def stopwordslist(filepath):
    stopwords = [line.strip() for line in open(filepath, 'r', encoding='gbk').readlines()]
    return stopwords

# 对句子去除停用词
def movestopwords(sentence):
    stopwords = stopwordslist('stop_words.txt')  # 这里加载停用词的路径
    outstr = ''
    for word in sentence:
        if word not in stopwords:
            if word != '\t'and'\n':
                outstr += word
                outstr += " "
    return outstr

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="2019my03sql31",
  database="toutiao"
)

mycursor=mydb.cursor()

mycursor.execute("SELECT id,title,abstract FROM information")

myresult=mycursor.fetchall()

# 过滤不了\\ \ 中文（）还有————
r1 = u'[a-zA-Z0-9’!"#$%&\'()*+,-./:;<=>?@，。?★、…【】《》？“”‘’！[\\]^_`{|}~]+'#用户也可以在此进行自定义过滤字符 
# 者中规则也过滤不完全
r2 = "[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*（）]+"
# \\\可以过滤掉反向单杠和双杠，/可以过滤掉正向单杠和双杠，第一个中括号里放的是英文符号，第二个中括号里放的是中文符号，第二个中括号前不能少|，否则过滤不完全
r3 =  "[.!//_,$&%^*()<>+\"'?@#-|:~{}]+|[——！\\\\，。=？、：“”‘’《》【】￥……（）]+" 
# 去掉括号和括号内的所有内容
r4 =  "\\【.*?】+|\\《.*?》+|\\#.*?#+|[.!/_,$&%^*()<>+""'?@|:~{}#]+|[——！\\\，。=？、：“”‘’￥……（）《》【】]"

for x in myresult:

    id=x[0]

    title=x[1]
    title=re.sub(r4,'',title)
    abstract=x[2]
    abstract=re.sub(r4,'',abstract)
    
    seg_list = jieba.cut(title, cut_all=False) # 分词精确模式
    # title=" ".join(seg_list)
    # print(title)
    title=movestopwords(seg_list)
    # print(title)

    seg_list = jieba.cut(abstract, cut_all=False)
    abstract=movestopwords(seg_list)
    # abstract=" ".join(seg_list)

    sql="UPDATE fenci SET title = %s, abstract = %s WHERE id = %s"
    val=(title,abstract,id)
    mycursor.execute(sql,val)

    # break

mydb.commit()