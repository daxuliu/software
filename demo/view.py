from . linkmysql import linkmysql
from . towords import towords
from . openkoapi import Judge
from . openkoapi import Passage
from . openkoapi import t
from django.http import HttpResponse
from . myemail import send
import json 
import qrcode
import time
import os
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect  

def blog(request):
        data=linkmysql("47.107.227.208","root","hismine","blog")
        article=data.getAllArticle()
         
#        return render(request, 'base.html',{"p":passage})
        return render(request, 'devblog/blog-list.html',{"articles":article})
def sendemail(request):
        address=request.GET.get("semail")
        from_addr = '1697935859@qq.com'
        password = 'yokhrbcxhllleceg'
        to_addr = []
        to_addr.append(address)
        data=linkmysql("47.107.227.208","root","hismine","blog")
        data.addemail(address)
        smtp_server = 'smtp.qq.com'
        send(from_addr, password, to_addr, smtp_server, 'Hi, my name is Kitsch. Briefly introduce yourself here. You can also provide a link to the about page.', 'Welcome!', 'Hi')
        return HttpResponseRedirect("../blog/")
def article(request):
        data=linkmysql("47.107.227.208","root","hismine","blog")
        id=request.GET.get("id")
        article=data.selectbyid(id)
         
#        return render(request, 'base.html',{"p":passage})
        return render(request, 'devblog/blog-post.html',{"a":article})
def index(request):
        data=linkmysql("47.107.227.208","root","hismine","blog")
        
        article=data.getAllArticle()
         
#        return render(request, 'base.html',{"p":passage})
        return render(request, 'devblog/index.html',{"articles":article})
def about(request):
        return render(request,"devblog/about.html")
def add(request):
    password=''
    title=request.POST.get('title','')
    content=request.POST.get('content','')
    code=request.POST.get('code','')
    intro=request.POST.get('intro','')
    password=request.POST.get('password','')
    if password=="fan":
        print(password)
        data=linkmysql("47.107.227.208","root","hismine","blog")
        
        data.addarticle(title=title,code=code,content=content,intro=intro)
        from_addr = '1697935859@qq.com'
        pd = 'yokhrbcxhllleceg'
        to_addr = data.getallemail()
        
        
        smtp_server = 'smtp.qq.com'
        send(from_addr, pd, to_addr, smtp_server, '您关注的Kitsch ,发布了新文章', '新品达到!', 'Hi')
        return HttpResponseRedirect("../blog/")
    else:
        return render(request,"403.html")
def myadmin(request):
    
    return render(request,"devblog/admin2.html")

def upload_imgs(request):
        if request.method == 'POST':
                newImg = request.FILES.get("upLoadImg", None)
                if not newImg:
                        return HttpResponse("没有图片被上传")
                destination = open(os.path.join(BASE_DIR,'static','images',newImg.name),'wb')
                for chunk in newImg.chunks():
                        destination.write(chunk)
                destination.close()
                return HttpResponse("成功上传")



