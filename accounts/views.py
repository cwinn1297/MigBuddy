from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegistrationForm, UserProfileForm


def index(request):
    return render(request, 'accounts/index.html')


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


@login_required
def settings(request):
    """User account settings page"""
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated successfully.')
            return redirect('accounts:settings')
    else:
        form = UserProfileForm(instance=request.user)
    
    return render(request, 'accounts/settings.html', {'form': form})
