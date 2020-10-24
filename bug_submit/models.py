from django.db import models
from django.contrib.auth.models import User


# class bug_type(models.Model):
#     text = models.CharField(max_length=200)  # CharField可以容纳不同文字
#     date_added = models.DateTimeField(auto_now_add=True)  # 为标题的创建加上时间
#     # bug_owner = models.ForeignKey(User,on_delete=models.CASCADE,related_name="bug_owner")  # 建立一个外键关系,dj3.0以上记得传on_delete
#
#     # 返回模型的字符串表示
#     def __str__(self):
#         return self.text


class bug_inform(models.Model):
    text = models.TextField()  # 这里要注意CharField和TextFiled之间的区别，TextFiled 传递max_length
    date_added = models.DateTimeField(auto_now_add=True)
    bug_owner = models.ForeignKey(User, on_delete=models.CASCADE)  # 建立一个外键关系,dj3.0以上记得传on_delete

    class Meta:
        verbose_name_plural = 'bug_informs'

    def __str__(self):
        return self.text[:40]
