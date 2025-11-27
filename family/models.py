from django.db import models
from django_countries.fields import CountryField
from accounts.models import User

# Create your models here.
class FamilyMember(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='family_members')
    FamilyMemberID = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    class Relationship(models.TextChoices):
        SELF = 'self', 'Self'
        SPOUSE = 'spouse', 'Spouse'
        FIANCEE = 'fiancée', 'Fiancée'
        CHILD = 'child', 'Child'
        PARENT = 'parent', 'Parent'
        SIBLING = 'sibling', 'Sibling'
    relationship = models.CharField(max_length=255, choices=Relationship.choices)
    date_of_birth = models.DateField()
    class Gender(models.TextChoices):
        MALE = 'male', 'Male'
        FEMALE = 'female', 'Female'
    gender = models.CharField(max_length=255, choices=Gender.choices)
    nationality = CountryField()
    passport_number = models.CharField(max_length=35)
    passport_expiry_date = models.DateField()
    passport_issue_date = models.DateField()
    passport_issue_country = CountryField()
    
    def get_full_name(self):
        """Return the full name of the family member."""
        return f"{self.first_name} {self.last_name}"
    
    def __str__(self):
        return f"{self.get_full_name()} ({self.get_relationship_display()})"