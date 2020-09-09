"""demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import view
from django.conf.urls import url
from . import settings
from django.conf.urls.static import static
from  app1 import views
from django.conf.urls.static import static
from . import settings

static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns = [
# path('admin/', admin.site.urls),
# path('blog/',view.blog),
# path('send/',view.sendemail),
# path('article/',view.article),
 path('index/',views.index)  ,
# path("about/",view.about)  ,
# path("add/",view.add),
path("login_action",views.login_action),
path("login",views.login),
path("upload",views.pic_handle),
path("register",views.register),
path("album",views.album),
path("user",views.get_user_img),
url(r'^pic_upload/$', views.pic_upload),
url(r'^pic_handle/$', views.pic_handle),
url(r'^pic_show/$', views.pic_show),]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)


