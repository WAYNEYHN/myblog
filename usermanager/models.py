from django.db import models


# Create your models here.
class UserInfo(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=53)
    email = models.EmailField()


class comment(models.Model):
    usr = models.ForeignKey("UserInfo", on_delete=True)
    # re_commend = models.ForeignKey("comment", on_delete=True)
    content = models.CharField(max_length=128)
    time = models.DateTimeField()