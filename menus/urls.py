from django.urls import path
from . import views


app_name = 'menus'

urlpatterns = [
    path('', views.public_menu_list, name='menu-list'),
]
