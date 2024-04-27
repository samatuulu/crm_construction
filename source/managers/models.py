from django.contrib.auth.models import AbstractUser
from django.db import models


class Managers(AbstractUser):
    phone = models.CharField(max_length=15)
    full_name = models.CharField(max_length=150)

    def __str__(self):
        return self.phone

    class Meta:
        swappable = 'AUTH_USER_MODEL'
