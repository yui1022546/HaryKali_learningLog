from django.contrib import admin

from my_blogs.models import *

admin.site.register(Topic)  #如果发现app里面没有相应的模块可以先看看这里有没有注册
admin.site.register(Entry)