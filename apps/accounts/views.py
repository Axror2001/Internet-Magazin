from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
# from django.contrib.auth.decorators import login_required


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request,user)
            
            if user.user_type == 'ADMIN':
                return redirect ('admin_dashboard')
            # elif user.user_type == 'STORE_ADMIN':
            #     return redirect ('store_admin_dashboard')
            # return redirect('store')
            return HttpResponse(
                f"Username: f{request.user.username}, User type: f{request.user.user_type}")
    else:
        form = AuthenticationForm()

    return render(request, 'users/login.html', {'form': form})


# @login_required

# @login_required
# def store_admin_dashboard(request):
#     return render(request,'users/store_admin_dashboard.html')

# def store(request):
#     return render(request,'users/store.html')

