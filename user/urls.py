from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.members_info, name='members_info'),
    path(
        'members/dashboard/',
        views.members_dashboard,
        name='members_dashboard'
        ),
    path('profile/', views.user_profile, name='user_profile'),
]
