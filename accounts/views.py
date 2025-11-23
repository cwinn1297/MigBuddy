from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from .forms import UserRegistrationForm


def index(request):
    return render(request, 'accounts/index.html')


def register(request):
    """User registration view"""
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created successfully for {username}! You are now logged in.')
            login(request, user)  # Automatically log in the user after registration
            return redirect('accounts:index')
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})
