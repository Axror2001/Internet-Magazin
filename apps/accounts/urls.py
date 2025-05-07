from django.urls import path
from apps.core.views import admin_dashboard, store_admin, index  # index ham import qilindi
from .views import my_login

urlpatterns = [
    path('', index, name='index'),  # index sahifasi (asosiy sahifa)
    path('login/', my_login, name='login'),
    path('admin_dashboard/', admin_dashboard, name='admin_dashboard'),
    path('store_admin/', store_admin, name='store_admin'),
]
