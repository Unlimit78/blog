from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    blog = models.OneToOneField('Blog',on_delete=models.SET_NULL,related_name='blog',null=True)
    subscribed = models.ManyToManyField('Blog',blank=True)
    is_readed = models.ManyToManyField('Post',blank=True)
    class Meta:
        pass
    def __str__(self):
        return self.username

class Blog(models.Model):
    title = models.CharField(max_length=100,default='')
    posts = models.ManyToManyField('Post',blank=True)
    class Meta:
        pass
    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    date_of_creation = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering =['-date_of_creation']
    def __str__(self):
        return self.title

