from django.db import models
from datetime import datetime
from django import forms


class user(models.Model):
    username=models.CharField(max_length=150)
    email=models.EmailField(max_length=150)
    password=models.CharField(max_length=60)
    timestamp=models.DateTimeField(auto_now=True)
