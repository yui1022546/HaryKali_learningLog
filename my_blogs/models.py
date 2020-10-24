from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField

class Topic(models.Model):
    text = models.CharField(max_length=200)  # CharField可以容纳不同文字
    date_added = models.DateTimeField(auto_now_add=True)  # 为标题的创建加上时间
    owner = models.ForeignKey(User,on_delete=models.CASCADE)  # 建立一个外键关系,dj3.0以上记得传on_delete

    # 返回模型的字符串表示
    def __str__(self):
        return self.text


class Entry(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text =RichTextUploadingField()  # 这里要注意CharField和TextFiled之间的区别，TextFiled 传递max_length
    date_added = models.DateTimeField(auto_now_add=True)

    # class meta是用来返回entries的负数表示
    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        return self.text[:40]
        # 返回这个类的str表示
