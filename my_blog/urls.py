"""my_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import *
from django.conf.urls import *

urlpatterns = [
    # path('admin/', admin.site.urls),

    url(r'', include(('my_blogs.urls', 'my_blogs'), namespace='my_blogs')),
    # django3,0的格式是url（include(("appurl地址"，“app名称”),namespace="app名称")）
    url(r'', include(("users.urls", "users"), namespace="users")),
    url(r'', include(("bug_submit.urls", "bug_submit"), namespace="bug_submit")),
    url('ckeditor/',include("ckeditor_uploader.urls"))

]
