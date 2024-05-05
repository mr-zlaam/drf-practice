from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Super user has to have is_staff being true")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Super user has to have is_superuser being true")
        return self.create_user(email=email, password=password, **extra_fields)


class User(AbstractUser):
    email = models.EmailField(unique=True, max_length=30)
    username = models.CharField(unique=True, max_length=10)
    date_of_birth = models.DateField(auto_now_add=False)
    objects = CustomUserManager()
