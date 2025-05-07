from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse


def my_login(request): 
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)  # foydalanuvchini sessiyaga kiritish

            # Agar foydalanuvchi store admin bo'lsa, store boshqaruv paneliga yo'naltirish
            if user.user_type == 'STORE_ADMIN':
                return redirect('store_admin')  # store admin paneliga yo‘naltirish
            
            # Agar foydalanuvchi admin bo'lsa, admin paneliga yo'naltirish
            elif user.user_type == 'ADMIN' or user.is_superuser:
                return redirect('admin_dashboard')  # admin paneliga yo‘naltirish
    else:
        form = AuthenticationForm()

    return render(request, 'accounts/login.html', {'form': form})


def index(request):
    return render(request, 'index.html')
