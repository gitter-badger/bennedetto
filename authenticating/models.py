from uuid import uuid4

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        user = self.model(email=email)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password):
        user = self.model(email=email)
        user.set_password(password)
        user.is_staff = True
        user.save()
        return user


class User(AbstractBaseUser):
    objects = UserManager()

    id = models.UUIDField(primary_key=True,
                          unique=True,
                          editable=False,
                          default=uuid4)

    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def get_full_name(self):
        return self.get_short_name()

    def get_short_name(self):
        return self.email

    def has_perm(self, *args, **kwargs):
        return self.is_staff

    def has_module_perms(self, *args):
        return self.is_staff
