from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('booking/', views.BookingCreateView.as_view(), name='booking_form'),
]
