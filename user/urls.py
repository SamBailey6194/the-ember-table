from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('', views.members_info, name='members_info'),
    path('custom-login/', views.custom_login, name='custom_login'),
    path('custom-signup/', views.custom_signup, name='custom_signup'),
    path('dashboard/', views.members_dashboard, name='members_dashboard'),
    path('logout/', views.custom_logout, name='custom_logout'),
]
