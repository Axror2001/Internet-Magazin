from django.db import models
from django.contrib.auth.models import AbstractUser


class EstoreUsers (AbstractUser):
    '''
    Django ni o'zini User modelini ustidan
    yozvoryabmiz, bizda 3 ta turdagi foydalanuvchi 
    boladi: Admin, Store Admin, Client
    '''

    USERS_TYPES_CHOICES = (
        ('ADMIN', 'Admin'),
        ('STORE_ADMIN', 'Store Admin'),
        ('Client', 'Client')
    )

    user_type = models.CharField(max_length=20, 
                                 choices=USERS_TYPES_CHOICES,
                                 default='Client')
    
    phone_number = models.CharField(max_length=15,
                                    blank=True,
                                    null=True)
    
    address = models.TextField(blank=True, null=True)
    
    def is_admin(self):
        return self.user_type == 'ADMIN' and self.is_superuser
    
    def is_store_admin(self):
        return self.user_type == 'STORE_ADMIN'
    
    def save (self, *args, **kwargs):
        self.set_password(self.password)
        super().save(*args, **kwargs)
        