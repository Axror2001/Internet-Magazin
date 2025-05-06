from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import ShopUser

@admin.register(ShopUser)
class ShopUserAdmin(UserAdmin):

    list_display = ('username', 'first_name', 'last_name', 'user_type', 'last_login')
    list_filter = ('user_type',)
    search_fields = ('username', 'first_name', 'last_name', 'user_type')
    ordering = ('-date_joined',)

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (('Personal Info'), {'fields': ('first_name', 'last_name')}),
        (('Shop Info'), {'fields': ('user_type',)}),
        (('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                      'groups', 'user_permissions')}),
        (('Important Dates'), {'fields': ('last_login', 'date_joined')}),

    )

    add_fieldsets = (
        (None, {
            'classes':'wide',
            'fields': ('username', 'password1', 'password2', 'user_type')}),

        (('Personal Info'), {
            'classes':'wide',
            'fields': ('first_name', 'last_name')}),

        (('Permissions'), {
            'classes':'wide',
            'fields': ('is_active', 'is_staff', 'is_superuser',
                       'groups','user_permissions')}),
    )