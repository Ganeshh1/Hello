from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    name=models.ForeignKey(User,on_delete=models.CASCADE)
    city=models.CharField(max_length=100)
    age=models.IntegerField(default=0)
    phone=models.BigIntegerField(default=0)
    degree=models.CharField(max_length=100)
    birthdate=models.DateTimeField(default=timezone.now)
    email=models.EmailField()
    image=models.ImageField(default='default.jpg',upload_to='profile_pics')
    def __str__(self):
        
        return str(self.name)    