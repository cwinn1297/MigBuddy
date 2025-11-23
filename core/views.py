from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def landing(request):
    return render(request, 'core/landing.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
    return render(request, 'core/login.html')

@login_required
def home(request):
    # TODO: When Application model is created, query user's applications here
    # applications = Application.objects.filter(user=request.user).order_by('-created_at')
    applications = []  # Placeholder until Application model is created
    
    context = {
        'applications': applications,
        'has_applications': len(applications) > 0,
        'applications_count': len(applications),
    }
    return render(request, 'core/home.html', context)

def logout_view(request):
    logout(request)
    return redirect('landing')