from django.db import models
from django.contrib.auth.models import AbstractUser #CustomerUser를 만들렬면 
# Create your models here.
class CustomUser(AbstractUser): #1:1 관계
    age = models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=50, null=True, blank=True)