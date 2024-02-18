from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


class MyUser(AbstractUser):
    is_sender = models.BooleanField(default=False)
    # groups = models.ManyToManyField(Group, related_name='myuser_groups')
    # user_permissions = models.ManyToManyField(Permission, related_name='myuser_user_permissions')

    def __str__(self):
        return self.username
