from django.db import models
from django.contrib.auth.models import User

import datetime

# Create your models here.
class ToDoItem(models.Model):
    date = models.DateTimeField(default=datetime.datetime.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=256)
    check = models.BooleanField(default=False)
