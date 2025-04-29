from django.db import models
from django.contrib.auth.models import AbstractUser


class Users (AbstractUser):
    USERS_TYPES = (
        ('ADMIN', 'Admin'),
        ('STORE_ADMIN', 'Store Admin'),
        ('USER', 'User')
    )

    user_type = models.CharField(max_length=20, choices=USERS_TYPES,
                                 default='USER')
    
    def is_admin(self):
        return self.user_type == 'ADMIN' and self.is_superuser
    
    def is_store_admin(self):
        return self.user_type == 'STORE_ADMIN'
    
    def save (self, *args, **kwargs):
        self.set_password(self.password)
        super().save(*args, **kwargs)
        