from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # pass
    nickname = models.fields.CharField(max_length=30, null=True)
    # add additional fields in here

    def __str__(self):
        return self.username