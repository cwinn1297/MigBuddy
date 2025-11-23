from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    phone = models.CharField(max_length=20, blank=True)
    middle_name = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return self.get_full_name() or self.username

