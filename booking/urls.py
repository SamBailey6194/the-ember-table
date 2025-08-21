from django.urls import path
from . import views

app_name = 'booking'

urlpatterns = [
    path('', views.booking_page, name='booking_page'),
    path('cancelled/', views.booking_cancelled, name='booking_cancelled'),
    path('cancel/', views.cancel_booking, name='cancel_booking'),
    path('makebooking/', views.make_booking, name='make_booking'),
    path('success/', views.success, name='success'),
    path('updated/<int:booking_id>/', views.update_booking, name='update'),
]
