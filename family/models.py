from django.db import models
from django_countries.fields import CountryField

# Create your models here.
class FamilyMember(models.Model):
    FamilyMemberID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
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