from django.urls import path
from . import views

app_name = 'booking'

urlpatterns = [
    path('', views.booking_page, name='booking_page'),
    path('cancelled/', views.booking_cancelled, name='booking_cancelled'),
    path('managebooking/', views.manage_booking, name='manage_booking'),
    path('makebooking/', views.make_booking, name='make_booking'),
    path('searchslots/', views.search_slots, name='search_slots'),
    path('success/', views.success, name='success'),
]
