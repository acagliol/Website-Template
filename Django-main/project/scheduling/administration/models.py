from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Administration (models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=30) #table
    description = models.TextField()
    date_created = models.DateTimeField()