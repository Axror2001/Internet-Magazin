from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login
from django.forms import forms
from .models import ShopUser


class ShopUserCreationForm(UserCreationForm):
    
    class Meta(UserCreationForm.Meta):
        model = ShopUser
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Username kiriting'
        })

        self.fields['first_name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Ism kiriting'
        })

        self.fields['last_name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Familiya kiriting'
        })

        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Parol kiriting'
        })

        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Parol tasdiqlang'
        })



def register(request):
    if request.method == 'POST':
        form = ShopUserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)

            return redirect('index')
        else:
            print(form.errors)
    else:
        form = ShopUserCreationForm()
    return render(request, "accounts/registration.html", {'form': form})



def my_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)

        
    else:
        form = AuthenticationForm()

    return render(request, "accounts/login.html", {'form': form})