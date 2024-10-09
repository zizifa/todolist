from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    id = models.AutoField(primary_key=True)
    user=models.CharField(max_length=50 )
    title = models.CharField(max_length=50,blank=True)
    discription = models.TextField(blank=True)
    complete=models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)

