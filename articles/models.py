from django.db import models
from datetime import datetime

# Create your models here.

class Category(models.Model):
    category = models.CharField(max_length=200)
    is_published = models.BooleanField(default=True)
    priority = models.IntegerField(default=1)
    def __str__(self):
        return self.category

class Content(models.Model):

    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    body = models.TextField(blank=False)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    published_date = models.DateTimeField(default=datetime.now, blank=True)
    is_published = models.BooleanField(default=True)
    priority = models.IntegerField(default=1)

    def __str__(self):
        return self.title

# class Comment(models.Model):
#     content = models.ForeignKey(Content, on_delete=models.DO_NOTHING)
#     your_name = models.CharField(max_length=100)  
#     is_outofservices = models.BooleanField(default=False)
#     is_comments =  models.BooleanField(default=True)
#     fp_num = models.IntegerField(default=16)
#     fp_max = models.IntegerField(default=999)
#     tp_num = models.IntegerField(default=16)
#     tp_max = models.IntegerField(default=999)
#     published_date = models.DateTimeField(default=datetime.now, blank=True)  
#     your_comment = models.TextField(max_length=200)
#     published_date = models.DateTimeField(default=datetime.now, blank=True)
#     is_published = models.BooleanField(default=True)
#     priority = models.IntegerField(default=1)

class Comment(models.Model):
    content = models.ForeignKey(Content, on_delete=models.DO_NOTHING)
    your_name = models.CharField(max_length=100)
    your_comment = models.TextField(max_length=200)
    published_date = models.DateTimeField(default=datetime.now, blank=True)
    is_published = models.BooleanField(default=True)
    priority = models.IntegerField(default=1)
    def __str__(self):
        return self.your_name
    
    def __str__(self):
        return self.your_name