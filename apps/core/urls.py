from django.urls import path
from .views import admin_dashboard, index

urlpatterns = [
    path('', index, name='index'),
    path('super/admin/', admin_dashboard, name='admin_dashboard'),
]