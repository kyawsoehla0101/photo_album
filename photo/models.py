from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
     user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
     name = models.CharField(max_length=50)

     def __str__(self):
          return self.name

class Photo(models.Model):
     category = models.ForeignKey(Category, on_delete=models.CASCADE)
     title = models.CharField(max_length=100)
     image = models.ImageField(upload_to='photo_album')

     def __str__(self):
          return self.title



