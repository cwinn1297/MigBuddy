from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Landing page
    path('', views.landing, name='landing'),
    
    # Authentication
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('password_reset/', views.password_reset, name='password_reset'),
    
    # Dashboard/Home (authenticated) - multiple aliases for template compatibility
    path('home/', views.home, name='home'),
    path('dashboard/', views.home, name='dashboard'),
]