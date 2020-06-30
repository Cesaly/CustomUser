from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
# Create your models here.


class MyUser(AbstractUser):
    homepage = models.URLField(max_length=100, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    display_name = models.CharField(max_length=50, null=True, blank=True)

    REQUIRED_FIELDS = ['homepage', 'age', 'display_name']
