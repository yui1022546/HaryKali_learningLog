from django.conf.urls import url,re_path
from . import views
from django.urls import path

urlpatterns = [

    url('^$', views.index, name='index'),
    url('^about.html', views.about, name="about.html"),
    url('^topics/$', views.topics, name="topics"),
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
    url(r'^new_topic/$',views.new_topic,name="new_topic"),
    url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
    url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry,
        name='edit_entry'),

    url('about.html$', views.about, name="about.html"),

    # url('topics/about.html|topics/./about.html', views.about, name="about.html"),
    # url('new_topic/about.html|new_topic/./about.html', views.about, name="about.html"),
    # url('new_entry/about.html|new_entry/./about.html', views.about, name="about.html"),
    # url('edit_entry/about.html|edit_entry/./about.html', views.about, name="about.html"),


]

