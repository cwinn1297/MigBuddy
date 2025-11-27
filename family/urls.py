from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    
    # Family Members
    path('', views.family_members, name='family_members'),

    # Family Member Details
    path('<int:FamilyMemberID>/details', views.family_member_details, name='family_member_details'),

    # Family Member Add
    path('add/', views.family_member_add, name='family_member_add'),
    
    # Family Member Delete
    path('<int:FamilyMemberID>/delete/', views.family_member_delete, name='family_member_delete'),
]