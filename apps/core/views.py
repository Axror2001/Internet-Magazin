from django.shortcuts import render


def admin_dashboard(request):
    return render(request,'core/admin_dashboard.html', {})


def index(request):
    return render(request, 'core/index.html', {})