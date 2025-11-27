from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from accounts.forms import UserRegistrationForm
from django.contrib import messages

# Create your views here.

def landing(request):
    return render(request, 'core/landing/home.html')

def register(request):
    """User registration view"""
    # If user is already logged in, redirect to home
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created successfully for {username}! You are now logged in.')
            # Specify backend since multiple authentication backends are configured
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'core/auth/register.html', {'form': form})

def password_reset(request):
    return render(request, 'core/auth/password_reset.html')


def login_view(request):
    # If user is already logged in, redirect to home
    if request.user.is_authenticated:
        return redirect('home')
    
    error_message = None
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')
        
        if username and password:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                error_message = "Invalid email or password. Please try again."
        else:
            error_message = "Please enter both email and password."
    
    context = {'error_message': error_message}
    return render(request, 'core/auth/login.html', context)

@login_required
def home(request):
    # TODO: When Application model is created, query user's applications here
    # applications = Application.objects.filter(user=request.user).order_by('-created_at')
    applications = []  # Placeholder until Application model is created
    
    context = {
        'applications': applications,
        'has_applications': len(applications) > 0,
        'applications_count': len(applications),
        'active': 'dashboard',
    }
    return render(request, 'core/app/dashboard.html', context)

def logout_view(request):
    logout(request)
    return redirect('landing')