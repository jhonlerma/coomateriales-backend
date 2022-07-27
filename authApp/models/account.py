from django.db import models
from .user import User

class Account(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, related_name='Account', on_delete=models.CASCADE)
    isActive = models.BooleanField(default=True)