from django.db import models

class Account(models.Model):
    """生成一个Account类"""
    username = models.CharField('用户名', max_length=30)
    password = models.CharField('密码', max_length=30)
    email = models.EmailField('电子邮箱', blank=True)
    desc = models.TextField('描述', max_length=500, blank=True)

    def __unicode__(self):
        return self.username
