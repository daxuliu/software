from django.shortcuts import render
from app1.models import IMG
from django.conf import settings
from django.http import HttpResponse
import time
from django.shortcuts import redirect
from .mydatabase import linkmysql
import json

data = linkmysql('ip', 'root', 'password', 'ruangong')
# Create your views here.
def check_user(func):
    def warpper(request, *args, **kwargs):
        if request.session.get('username', False):
            return func(request, *args, **kwargs)

        else:
            return redirect("/login")

    return warpper


def login(request):
    return render(request, 'page/loginform.html')


def login_action(request):
    username = request.POST.get("username")
    password = request.POST.get("pwd")

    userpw = data.user_selectByUserName(username)
    if len(userpw) == 0:
        return render(request, 'page/loginform.html')
    if password == userpw[0][0]:
        request.session["username"] = username
        return render(request, 'page/home.html')
    else:
        return render(request, 'page/loginform.html')

    request.session["login_user"] = username
    return render(request, 'page/loginform.html')


def index(request):
    return render(request, 'page/home.html')


# @check_user
def pic_upload(request):
    return render(request, 'pic_upload.html')



def pic_handle(request):
    f1 = request.FILES.get('file')
    username = request.POST.get("name")  # 从前端获取上传的图片
    fname = '{}/booktest/{}'.format(settings.MEDIA_ROOT, f1.name)  # 图片的完整路径
    with open(fname, 'wb') as pic:  # 文件操作
        for c in f1.chunks():  # 因为图片存储的方式是二进制流，用f1.chunks()获取图片的字节
            pic.write(c)
        #     img = IMG(img = f1)
        #     img.save()

    userid=data.getuserid(username)[0][0]


    data.Img_add(fname, username, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))#写入img表
    imgid=data.top_img()[0][0]
    data.user_addImg(userid,imgid)#写入img_user表

    # 这里写把照片的相关信息写入数据库的语句
    return HttpResponse('OK')


# @check_user
def pic_show(request):
    pic = IMG.objects.get(request.get('name'))
    context = {'pic': pic}
    return render(request, 'pic_show.html', context)


def register(request):
    username = request.POST.get("username")
    password = request.POST.get("pwd")

    res = data.user_selectByUserName(username)
    if len(res) == 0:
        data.user_addUser(username,password)
        return HttpResponse('True')
    else:
        return HttpResponse('False')
def album(request):
    res=data.album_select()
def get_user_img(request):
    try:
        username = request.GET.get("username")

        res=data.user_img(username)
        return HttpResponse(json.dumps(res,ensure_ascii=False),content_type="application/json,charset=utf-8")
    except:
        return HttpResponse(json.dumps([], ensure_ascii=False), content_type="application/json,charset=utf-8")


