from django.db import models
from django.contrib.auth.models import User

class review ( models.Model) :    #model is represented by a class in django, inherting Model from models class

    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='default.png', blank=True)
    author =  models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    bookAuth = models.CharField(max_length = 100)

    def __str__(self) : 
        return self.title 

    def snippet(self) :
        return self.body[:50] + " ..."   #takes first 50 char of the string