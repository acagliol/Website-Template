from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Counselor (models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=30) #table
    description = models.TextField()
    date_created = models.DateTimeField()