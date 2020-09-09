from django.shortcuts import render

# Create your views here.

from django.conf.urls import url
 
from . import view
 
urlpatterns = [
    url(r'^$', view.hello),
    url(r'^$', view.exa),
    url(r'^$', view.img),
    url(r'^$',view.addgood),
    url(r'^$',view.change),
     url(r'^$',view.select),
url(r'^$',view.judge),url(r'^$',view.Passages),
]
