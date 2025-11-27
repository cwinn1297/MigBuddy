from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .models import FamilyMember
from .forms import FamilyMemberForm

# Create your views here.
def family_members(request):
    family_members_list = FamilyMember.objects.filter(user=request.user)
    return render(request, 'family/family_list.html', {
        'active': 'family',
        'family_members': family_members_list
    })

def family_member_details(request, FamilyMemberID):
    # Get the family member and ensure it belongs to the current user
    member = get_object_or_404(FamilyMember, FamilyMemberID=FamilyMemberID, user=request.user)
    
    # Check if we're in edit mode
    edit_mode = request.GET.get('edit', '0') == '1'
    
    if request.method == 'POST':
        form = FamilyMemberForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            # Redirect to read-only view after saving
            return redirect('family_member_details', FamilyMemberID=FamilyMemberID)
    else:
        form = FamilyMemberForm(instance=member)
    
    return render(request, 'family/member_details.html', {
        'active': 'family',
        'member': member,
        'form': form,
        'edit_mode': edit_mode
    })

def family_member_add(request):
    if request.method == 'POST':
        form = FamilyMemberForm(request.POST)
        if form.is_valid():
            family_member = form.save(commit=False)
            family_member.user = request.user
            family_member.save()
            return redirect('family_members')
    else:
        form = FamilyMemberForm()
    return render(request, 'family/family_member_add.html', {'form': form, 'active': 'family'})

def family_member_delete(request, FamilyMemberID):
    # Get the family member and ensure it belongs to the current user
    member = get_object_or_404(FamilyMember, FamilyMemberID=FamilyMemberID, user=request.user)
    
    if request.method == 'POST':
        member.delete()
        return redirect('family_members')
    
    # If GET request, show confirmation (optional - you can redirect directly if preferred)
    return redirect('family_members')