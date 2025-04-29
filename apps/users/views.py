from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request,user)
            
            if user.user_type == 'ADMIN':
                return redirect ('admin_dashboard')
            elif user.user_type == 'STORE_ADMIN':
                return redirect ('store_admin_dashboard')
            
            return redirect('store')
    else:
        form = AuthenticationForm()

    return render(request, 'users/login.html', {'form': form})


@login_required
def admin_dashboard(request):
    return render(request,'users/admin_dashboard.html')

@login_required
def store_admin_dashboard(request):
    return render(request,'users/store_admin_dashboard.html')

def store(request):
    return render(request,'users/store.html')

