from django.urls import path
from . import views

app_name = 'forms'

urlpatterns = [
    path('', views.form_list, name='form_list'),
    path('open_form/', views.open_form, name='open_form'),
    path('open_form/<str:filename>/', views.open_form, name='open_form'),
]