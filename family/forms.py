from django import forms
from .models import FamilyMember
from django_countries import countries

class FamilyMemberForm(forms.ModelForm):
    # Override country fields to use regular Select widget
    nationality = forms.ChoiceField(
        choices=[('', 'Select a country')] + list(countries),
        widget=forms.Select(attrs={
            'class': 'w-full h-12 px-4 rounded-lg border border-gray-300 dark:border-white/20 bg-white dark:bg-white/5 text-[#333333] dark:text-gray-100 focus:outline-none focus:ring-2 focus:ring-primary/50 focus:border-primary/50 text-base font-normal leading-normal'
        })
    )
    
    passport_issue_country = forms.ChoiceField(
        choices=[('', 'Select a country')] + list(countries),
        widget=forms.Select(attrs={
            'class': 'w-full h-12 px-4 rounded-lg border border-gray-300 dark:border-white/20 bg-white dark:bg-white/5 text-[#333333] dark:text-gray-100 focus:outline-none focus:ring-2 focus:ring-primary/50 focus:border-primary/50 text-base font-normal leading-normal'
        })
    )
    
    class Meta:
        model = FamilyMember
        fields = ['first_name', 'middle_name', 'last_name', 'relationship', 'date_of_birth', 'gender', 'nationality', 'passport_number', 'passport_expiry_date', 'passport_issue_date', 'passport_issue_country']
        exclude = ['user']  # User is set automatically in the view
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'w-full h-12 px-4 rounded-lg border border-gray-300 dark:border-white/20 bg-white dark:bg-white/5 text-[#333333] dark:text-gray-100 focus:outline-none focus:ring-2 focus:ring-primary/50 focus:border-primary/50 placeholder:text-gray-400 dark:placeholder:text-gray-500 text-base font-normal leading-normal',
                'placeholder': 'First name'
            }),
            'middle_name': forms.TextInput(attrs={
                'class': 'w-full h-12 px-4 rounded-lg border border-gray-300 dark:border-white/20 bg-white dark:bg-white/5 text-[#333333] dark:text-gray-100 focus:outline-none focus:ring-2 focus:ring-primary/50 focus:border-primary/50 placeholder:text-gray-400 dark:placeholder:text-gray-500 text-base font-normal leading-normal',
                'placeholder': 'Middle name'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'w-full h-12 px-4 rounded-lg border border-gray-300 dark:border-white/20 bg-white dark:bg-white/5 text-[#333333] dark:text-gray-100 focus:outline-none focus:ring-2 focus:ring-primary/50 focus:border-primary/50 placeholder:text-gray-400 dark:placeholder:text-gray-500 text-base font-normal leading-normal',
                'placeholder': 'Last name'
            }),
            'relationship': forms.Select(attrs={
                'class': 'w-full h-12 px-4 rounded-lg border border-gray-300 dark:border-white/20 bg-white dark:bg-white/5 text-[#333333] dark:text-gray-100 focus:outline-none focus:ring-2 focus:ring-primary/50 focus:border-primary/50 text-base font-normal leading-normal'
            }),
            'date_of_birth': forms.DateInput(attrs={
                'type': 'date',
                'class': 'w-full h-12 px-4 rounded-lg border border-gray-300 dark:border-white/20 bg-white dark:bg-white/5 text-[#333333] dark:text-gray-100 focus:outline-none focus:ring-2 focus:ring-primary/50 focus:border-primary/50 text-base font-normal leading-normal'
            }),
            'gender': forms.Select(attrs={
                'class': 'w-full h-12 px-4 rounded-lg border border-gray-300 dark:border-white/20 bg-white dark:bg-white/5 text-[#333333] dark:text-gray-100 focus:outline-none focus:ring-2 focus:ring-primary/50 focus:border-primary/50 text-base font-normal leading-normal'
            }),
            'passport_number': forms.TextInput(attrs={
                'class': 'w-full h-12 px-4 rounded-lg border border-gray-300 dark:border-white/20 bg-white dark:bg-white/5 text-[#333333] dark:text-gray-100 focus:outline-none focus:ring-2 focus:ring-primary/50 focus:border-primary/50 placeholder:text-gray-400 dark:placeholder:text-gray-500 text-base font-normal leading-normal',
                'placeholder': 'Passport number'
            }),
            'passport_expiry_date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'w-full h-12 px-4 rounded-lg border border-gray-300 dark:border-white/20 bg-white dark:bg-white/5 text-[#333333] dark:text-gray-100 focus:outline-none focus:ring-2 focus:ring-primary/50 focus:border-primary/50 text-base font-normal leading-normal'
            }),
            'passport_issue_date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'w-full h-12 px-4 rounded-lg border border-gray-300 dark:border-white/20 bg-white dark:bg-white/5 text-[#333333] dark:text-gray-100 focus:outline-none focus:ring-2 focus:ring-primary/50 focus:border-primary/50 text-base font-normal leading-normal'
            }),
        }