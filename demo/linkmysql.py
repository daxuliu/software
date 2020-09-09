import pymysql
from  .article import  Article
class linkmysql:
    def __init__(self,ip,user,password,database):
        self.db=pymysql.connect(ip,user,password,database)
        self.cursor=self.db.cursor()

    def select(self):

        sql = 'select * from article '
        self.cursor.execute(sql)
        res = self.cursor.fetchall()
        return res
    def getallemail(self):

        sql = 'select * from email '
        self.cursor.execute(sql)
        res = self.cursor.fetchall()
        re=[]
        for i in res:
            re.append(i[-1])
        return re
    def selectbyid(self,id):

        sql = 'select * from article  where id =%s '
        self.cursor.execute(sql,(id))
        res = self.cursor.fetchall()
        articles = []
        for i in res:
            a = Article(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8])
            articles.append(a)
        return articles[0]
    def getAllArticle(self):
        res=self.select()
        articles=[]
        for i in res:
            a=Article(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8])
            articles.append(a)
        return  articles
    def addarticle(self, content="",date="",time="",comment="",intro="",imgsrc="",title="",code=""):

        insertsql = "INSERT INTO article(content,date,time,comment,imgsrc,title,intro,code) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
        self.cursor.execute(insertsql, (content,date,time,comment,imgsrc,title,intro,code))
        self.db.commit()
    def addemail(self,address):
        sql="INSERT INTO email(address) VALUES(%s)"
        self.cursor.execute(sql, (address))
        self.db.commit()
if  __name__ == '__main__':
    linkmysql=linkmysql("47.107.227.208","root","hismine","blog")

    res=linkmysql.selectbyid(1)
    print(res.code)