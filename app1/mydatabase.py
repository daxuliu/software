import time

import pymysql

class linkmysql:
    def __init__(self, ip, user, password, database):
        self.db = pymysql.connect(ip, user, password, database)
        self.cursor = self.db.cursor()
    #查询所有
    def album_select(self):
        sql = 'select * from album'
        self.cursor.execute(sql)
        res = self.cursor.fetchall()
        print(res)
        return res
    #插入相册
    def album_addalbum(self,albumName="",albumUrl="",date=""):
        insertsql = "INSERT INTO album (albumName, albumUrl, date) VALUES (%s, %s, %s)"
        self.cursor.execute(insertsql, (albumName, albumUrl, date))
        self.db.commit()
    #按照album名字查询
    def album_selectByName(self,albumName=""):
        sql = 'select * from album where albumName = %s'
        self.cursor.execute(sql,(albumName))
        res = self.cursor.fetchall()
        print(res)
        return res
    #按照相册名字删除
    def album_deleteByName(self,albumName=""):
        delsql = "DELETE FROM album WHERE albumName= %s"
        self.cursor.execute(delsql,(albumName))
        self.db.commit()
    #添加相册描述
    def album_addDesc(self,albumId="",desc=""):
        insertsql = "INSERT INTO album_desc VALUES (%s, %s)"
        self.cursor.execute(insertsql, (albumId, desc))
        self.db.commit()
    #修改相册描述
    def album_UpdateDesc(self,desc="",albumId=""):
        sql = "UPDATE album_desc SET album_desc.desc = %s WHERE albumId = %s"
        self.cursor.execute(sql, (desc,albumId))
        self.db.commit()
    #删除相册描述
    def album_deleteDesc(self,albumId=""):
        sql = "delete from album_desc where albumId = %s"
        self.cursor.execute(sql, (albumId))
        self.db.commit()
    #查询相册描述
    def album_selectDescById(self,albumId=""):
        sql="select album_desc.desc from album_desc where albumId = %s"
        self.cursor.execute(sql,(albumId))
        res = self.cursor.fetchall()
        print(res)
        return res
    #添加用户绑定的相册
    def user_addAlbum(self,albumId="",userId=""):
        sql="INSERT INTO album_user VALUES (%s, %s)"
        self.cursor.execute(sql, (albumId, userId))
        self.db.commit()
    #删除用户绑定的相册
    def user_deleteAlbum(self,albumId=""):
        sql="delete from album_user where albumId = %s"
        self.cursor.execute(sql, (albumId))
        self.db.commit()
    #修改用户绑定的相册
    def user_updateAlbum(self,userId="",albumId=""):
        sql="UPDATE album_user SET album_user.userId = %s WHERE albumId = %s"
        self.cursor.execute(sql, (userId, albumId))
        self.db.commit()
    #查询用户绑定的相册id
    def user_selectAlbumIdByUserId(self,userId=""):
        sql="select albumId from album_user where userId=%s"
        self.cursor.execute(sql, (userId))
        res = self.cursor.fetchall()
        print(res)
        return res
    # 查询用户绑定的相册名称
    def user_selectAlbumNameByUserId(self,userId=""):
        sql = "select albumName from album where albumId = (select albumId from album_user where userId = %s)"
        self.cursor.execute(sql, (userId))
        res = self.cursor.fetchall()
        print(res)
        return res
    #查询相册绑定的用户名
    def user_selectUserNameByAlbumId(self, albumId=""):
        sql ="select userName from user where userId = (select userId from album_user where albumId = %s)"
        self.cursor.execute(sql, (albumId))
        res = self.cursor.fetchall()
        print(res)
        return res
    #查询相册中的图片名称
    def album_selectImgNameByAlbumId(self,albumId=""):
        sql="select imgName from imgs where imgId in (select imgId from album_img where albumId =%s)"
        self.cursor.execute(sql, (albumId))
        res = self.cursor.fetchall()
        print(res)
        return res
    #查询相册中的图片Url
    def album_selectImgUrlByAlbumId(self,albumId=""):
        sql="select imgUrl from imgs where imgId in (select imgId from album_img where albumId =%s)"
        self.cursor.execute(sql, (albumId))
        res = self.cursor.fetchall()
        print(res)
        return res
    #向相册中添加图片
    def album_addImg(self,albumId="",imgId=""):
        sql = "insert into album_img values( %s , %s)"
        self.cursor.execute(sql, (albumId,imgId))
        self.db.commit()
    #删除相册中的图片
    def album_deleteImg(self,albumId="",imgId=""):
        sql = "delete from album_img where albumId=%s and imgId=%s"
        self.cursor.execute(sql, (albumId,imgId))
        self.db.commit()
    #添加图片(图片上传）
    def Img_add(self,imgUrl="",imgName="",date=""):
        sql ="insert into imgs (imgUrl, imgName, date) values (%s,%s,%s)"
        self.cursor.execute(sql, (imgUrl,imgName,date))
        self.db.commit()
    #修改图片名
    def Img_updateName(self,imgName ="",imgId=""):
        sql="update imgs set imgName=%s where imgId=%s"
        self.cursor.execute(sql, (imgName,imgId))
        self.db.commit()
    #删除图片
    def img_select(self):
        sql = 'select * from imgs'
        self.cursor.execute(sql)
        res = self.cursor.fetchall()
        print(res)
        return res
    def Img_deleteImg(self,imgId=""):
        sql = "delete from imgs where imgId = %s"
        self.cursor.execute(sql, (imgId))
        self.db.commit()
    #用户注册（添加用户信息）
    def user_addUser(self,userName = "",pswd=""):
        sql = "insert into user(username, pswd) VALUES (%s,%s)"
        self.cursor.execute(sql, (userName,pswd))
        self.db.commit()
    #修改密码
    def user_updatePswd(self,pswd = "",userName=""):
        sql="update user set pswd = %s where userName = %s"
        self.cursor.execute(sql, (pswd,userName))
        self.db.commit()
    #按照用户名查询密码(登录时验证密码正误）
    def user_selectByUserName(self,userName=""):
        sql = "select pswd from user where userName = %s"
        self.cursor.execute(sql, (userName))
        res = self.cursor.fetchall()
        print(res)
        return res
    #添加用户上传的图片(用户上传图片时绑定）
    def user_addImg(self,userId="",imgId=""):
        sql = "insert user_img values (%s,%s)"
        self.cursor.execute(sql, (userId, imgId))
        self.db.commit()
    #按用户ID查询该用户上传的图片
    def user_selectImgById(self,userId=""):
        sql = "select imgId from user_img where userId = %s"
        self.cursor.execute(sql, (userId))
        res = self.cursor.fetchall()
        print(res)
        return res
    #点赞事件————添加相册点赞记录（建议创建相册时置零）
    def album_addPraise(self,albumId="",praiseNum=""):
        sql="insert praise values (%s,%s)"
        self.cursor.execute(sql, (albumId, praiseNum))
        self.db.commit()
    #点赞事件————修改点赞数
    def album_updatePraise(self,praiseNum="",albumId=""):
        sql = "update praise set praiseNum = %s where albumId = %s"
        self.cursor.execute(sql, (praiseNum,albumId))
        self.db.commit()
    #转发事件————添加相册转发记录
    def album_addSend(self,albumId="",sendNum=""):
        sql="insert send values (%s,%s)"
        self.cursor.execute(sql, (albumId, sendNum))
        self.db.commit()
    #转发事件————修改转发数
    def album_updateSend(self,sendNum="",albumId=""):
        sql = "update send set sendNum = %s where albumId = %s"
        self.cursor.execute(sql, (sendNum,albumId))
        self.db.commit()
#从album拿到所有的albumId 然后再从album_user 拿到所有的userId 然后在拿到所有的图片
    def album_user_img(self):
        sql = "select imgUrl from imgs where imgId in(select imgId from user_img where userId IN(select userId from album_user where albumId IN(select albumId from album)))"
        self.cursor.execute(sql)
        res = self.cursor.fetchall()
        print(res)
        return res
    # 从album拿到所有的albumId 然后再从album_user 拿到所有的userId
    def album_user(self):
        sql = "select username from user where userId in  (select userId from album_user where albumId IN(select albumId from album))"
        self.cursor.execute(sql)
        res = self.cursor.fetchall()
        print(res)
        return res
    def top_img(self):
        sql = "select count(*) from imgs"
        self.cursor.execute(sql)
        res = self.cursor.fetchall()
        print(res)
        return res
    def user_img(self,username):
        sql = "select * from imgs where imgId in (select imgId from user_img where userId =(select userId from user where username=%s))"
        self.cursor.execute(sql,(username))
        res = self.cursor.fetchall()
        print(res)
        # dic={"src": 'statics/images/1.png', "desc": '这是图片的描述', "date": 'time1'}
        reslist=[]
        for i in res:
            dic = {"src": 'statics/images/1.png', "desc": '这是图片的描述', "date": 'time1'}
            dic['src']=i[1]
            dic["desc"]=i[5]
            dic['date']=str(i[3])
            reslist.append(dic)
        return reslist
    def getuserid(self,name):
        sql = "select userId from user where  username= % s"
        self.cursor.execute(sql,(name))
        res = self.cursor.fetchall()
        print(res)
        return res
if __name__ == '__main__':
    pass
    #linkmysql.album_select()
    # time1 = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    #linkmysql.album_addalbum("12","2131",time1)
    #linkmysql.album_selectByName("1")
    #linkmysql.album_deleteByName("12")
    #linkmysql.album_addDesc("2", "asdasd")
    #linkmysql.album_UpdateDesc("asd","2")
    #linkmysql.album_deleteDesc("13")
    #linkmysql.album_selectDescById("1")
    #linkmysql.user_addAlbum("11","1")
    #linkmysql.user_deleteAlbum("11")
    #linkmysql.user_updateAlbum("2","21")
    #linkmysql.user_selectAlbumIdByUserId("1")
    #linkmysql.user_selectAlbumNameByUserId("1")
    #linkmysql.user_selectUserNameByAlbumId("1")
    #linkmysql.album_selectImgNameByAlbumId("1")
    #linkmysql.album_selectImgUrlByAlbumId("1")
    #linkmysql.album_addImg("3","1")
    #linkmysql.album_deleteImg("3","1")
    # linkmysql.Img_add("231","img4",time1)
    #linkmysql.Img_updateName("name1","1")
    #linkmysql.Img_deleteImg("3")
    # linkmysql.user_addUser("admin","123")
    #linkmysql.user_updatePswd("1234","user1")
    #linkmysql.user_selectByUserName("user1")
    #linkmysql.user_addImg("1","3")
    #linkmysql.user_selectImgById("1")
    #linkmysql.album_addPraise("3","0")
    #linkmysql.album_updatePraise("2","1")
    #linkmysql.album_addSend("1","0")
    #linkmysql.album_updateSend("3","1")
    # print(linkmysql.album_user_img())
    # print(linkmysql.top_img())
    # print(linkmysql.getuserid("admin"))
    # print(linkmysql.album_user())用户名
    # print(str(linkmysql.user_img('user2')))
    #
