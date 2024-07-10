from django.db import models

# Create your models here.

class user(models.Model):
    username = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=64)
    creationtime = models.DateTimeField(auto_now_add=True)
    userdescription = models.CharField(max_length=250)
    
    def __str__(self) -> str:
        return self.username
