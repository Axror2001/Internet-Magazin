from django.db import models
from django.contrib.auth.models import AbstractUser
    
    
class ShopUser (AbstractUser):
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

    user_type = models.CharField(max_length=20, choices=USERS_TYPES_CHOICES, default='CLIENT')    
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)

    def  __str__(self):
        return f'{self.first_name} {self.last_name}'