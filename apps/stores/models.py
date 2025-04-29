from django.db import models
from apps.users.models import Users


class Store(models.Model):
    name =models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    addreess = models.TextField(blank=True, null=True)
    phone_number = models.CharField(max_length=15)

    admin = models.OneToOneField(Users, related_name='store_admin',
                                 limit_choices_to={'user_type': 'STORE_ADMIN'},
                                 on_delete=models.CASCADE)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)


class Meta:
    ordering = ['name']

@property
def store_admin(self):
    return self.admin.get_full_name()