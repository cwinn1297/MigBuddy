from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()


class UserProfileForm(forms.ModelForm):
    """Form for updating user profile information"""
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
        widgets = {
            'first_name': forms.TextInput(attrs={
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

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

