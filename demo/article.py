import pymysql
class Article:
    def __init__(self,id,content,date,time,comment,imgsrc,title,intro,code):
       self.content=content
       self.date=date
       self.time=time
       self.intro=intro
       self.comment=comment
       self.id=id
       self.imgsrc=imgsrc
       self.title=title
       self.code=code