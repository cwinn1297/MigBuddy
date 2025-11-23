from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class UserProfileForm(forms.ModelForm):
    """Form for updating user profile information"""
    class Meta:
        model = User
        fields = ('first_name', 'middle_name', 'last_name', 'email', 'phone')
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'w-full rounded-md border-gray-300 dark:border-gray-600 dark:bg-gray-700 dark:text-white focus:border-primary focus:ring-primary',
            }),
            'middle_name': forms.TextInput(attrs={
                'class': 'w-full rounded-md border-gray-300 dark:border-gray-600 dark:bg-gray-700 dark:text-white focus:border-primary focus:ring-primary',
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'w-full rounded-md border-gray-300 dark:border-gray-600 dark:bg-gray-700 dark:text-white focus:border-primary focus:ring-primary',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'w-full rounded-md border-gray-300 dark:border-gray-600 dark:bg-gray-700 dark:text-white focus:border-primary focus:ring-primary',
            }),
            'phone': forms.TextInput(attrs={
                'class': 'w-full rounded-md border-gray-300 dark:border-gray-600 dark:bg-gray-700 dark:text-white focus:border-primary focus:ring-primary',
            }),
        }


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'class': 'w-full h-12 px-4 rounded-lg border border-gray-300 dark:border-white/20 bg-white dark:bg-white/5 text-[#333333] dark:text-gray-100 focus:outline-none focus:ring-2 focus:ring-primary/50 focus:border-primary/50 placeholder:text-gray-400 dark:placeholder:text-gray-500 text-base font-normal leading-normal',
        'placeholder': 'Enter your email address'
    }))
    first_name = forms.CharField(max_length=150, required=True, widget=forms.TextInput(attrs={
        'class': 'w-full h-12 px-4 rounded-lg border border-gray-300 dark:border-white/20 bg-white dark:bg-white/5 text-[#333333] dark:text-gray-100 focus:outline-none focus:ring-2 focus:ring-primary/50 focus:border-primary/50 placeholder:text-gray-400 dark:placeholder:text-gray-500 text-base font-normal leading-normal',
        'placeholder': 'First name'
    }))
    last_name = forms.CharField(max_length=150, required=True, widget=forms.TextInput(attrs={
        'class': 'w-full h-12 px-4 rounded-lg border border-gray-300 dark:border-white/20 bg-white dark:bg-white/5 text-[#333333] dark:text-gray-100 focus:outline-none focus:ring-2 focus:ring-primary/50 focus:border-primary/50 placeholder:text-gray-400 dark:placeholder:text-gray-500 text-base font-normal leading-normal',
        'placeholder': 'Last name'
    }))
    middle_name = forms.CharField(max_length=150, required=False, widget=forms.TextInput(attrs={
        'class': 'w-full h-12 px-4 rounded-lg border border-gray-300 dark:border-white/20 bg-white dark:bg-white/5 text-[#333333] dark:text-gray-100 focus:outline-none focus:ring-2 focus:ring-primary/50 focus:border-primary/50 placeholder:text-gray-400 dark:placeholder:text-gray-500 text-base font-normal leading-normal',
        'placeholder': 'Middle name (optional)'
    }))
    phone = forms.CharField(max_length=20, required=False, widget=forms.TextInput(attrs={
        'class': 'w-full h-12 px-4 rounded-lg border border-gray-300 dark:border-white/20 bg-white dark:bg-white/5 text-[#333333] dark:text-gray-100 focus:outline-none focus:ring-2 focus:ring-primary/50 focus:border-primary/50 placeholder:text-gray-400 dark:placeholder:text-gray-500 text-base font-normal leading-normal',
        'placeholder': 'Phone number (optional)'
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'w-full h-12 px-4 rounded-lg border border-gray-300 dark:border-white/20 bg-white dark:bg-white/5 text-[#333333] dark:text-gray-100 focus:outline-none focus:ring-2 focus:ring-primary/50 focus:border-primary/50 placeholder:text-gray-400 dark:placeholder:text-gray-500 text-base font-normal leading-normal',
        'placeholder': 'Username'
    }))
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={
            'class': 'w-full h-12 px-4 pr-12 rounded-lg border border-gray-300 dark:border-white/20 bg-white dark:bg-white/5 text-[#333333] dark:text-gray-100 focus:outline-none focus:ring-2 focus:ring-primary/50 focus:border-primary/50 placeholder:text-gray-400 dark:placeholder:text-gray-500 text-base font-normal leading-normal',
            'placeholder': 'Create a strong password'
        })
    )
    password2 = forms.CharField(
        label='Password confirmation',
        widget=forms.PasswordInput(attrs={
            'class': 'w-full h-12 px-4 pr-12 rounded-lg border border-gray-300 dark:border-white/20 bg-white dark:bg-white/5 text-[#333333] dark:text-gray-100 focus:outline-none focus:ring-2 focus:ring-primary/50 focus:border-primary/50 placeholder:text-gray-400 dark:placeholder:text-gray-500 text-base font-normal leading-normal',
            'placeholder': 'Re-enter your password'
        })
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'middle_name', 'last_name', 'email', 'phone', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.middle_name = self.cleaned_data.get('middle_name', '')
        user.phone = self.cleaned_data.get('phone', '')
        if commit:
            user.save()
        return user

