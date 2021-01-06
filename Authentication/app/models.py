from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    degree = models.CharField(max_length=1000,default='')
    description = models.TextField(default='')
    age = models.CharField(max_length=100,default= '')
    created_at = models.DateTimeField(auto_now_add=True)
