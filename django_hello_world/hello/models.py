from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birthday = models.DateField()
    email = models.EmailField()
    jabber = models.CharField(max_length=30)
    skype = models.CharField(max_length=30)
    bio = models.TextField()
    contacts = models.TextField()


class ReqData(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    path = models.CharField(max_length=2048)
    get = models.TextField()
    post = models.TextField()
    cookies = models.TextField()
