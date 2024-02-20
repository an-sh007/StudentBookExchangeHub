# myapp/models.py
from django.db import models

class UserAccount(models.Model):
		username = models.CharField(max_length=100)
		password = models.CharField(max_length=100)
