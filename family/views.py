from django.shortcuts import render
from .models import FamilyMember

# Create your views here.
def family_members(request):
    return render(request, 'family/family_list.html')

def family_member_details(request, FamilyMemberID):
    return render(request, 'family/member_details.html')

def family_member_add(request):
    return render(request, 'family/family_member_add.html')