from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def admin_dashboard(request):
    return render(request,'core/admin_dashboard.html', {})

def store_admin(request):
    return render(request, "core/store_admin.html", {})

def index(request):
    return render(request, 'core/index.html', {})