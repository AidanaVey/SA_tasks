from django.db import models

# Create your models here.
class UserList(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    mobile = models.CharField(max_length=12)
