from django.contrib import admin
from django.urls import path, include
# from apps.users.views import login_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.users.urls')),
    # path ('', login_view, name='home')
]
