from django.conf.urls import url
from django.contrib.auth.views import LoginView

from . import views

urlpatterns = [

    url(r'submit.html/$',views.submit, name="submit"),
    url(r'discuss.html/$', views.discuss, name='discuss'),

]
