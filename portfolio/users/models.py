from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class User(AbstractBaseUser):
    name = models.CharField(null=False, max_length=50)
    email = models.EmailField(blank=True, max_length=125)
    address = models.CharField(blank=True, max_length=125)
    profile_image = models.CharField(max_length=255, blank=False)
    phone_number = models.CharField(blank=True, max_length=25)
    description = models.TextField(blank=True),
    git_hub_link = models.CharField(blank=True, max_length=255)

    USERNAME_FIELD = 'name'
    REQUIRED_FIELDS = []
