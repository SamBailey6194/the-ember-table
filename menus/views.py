from django.shortcuts import render, get_object_or_404
from .models import Menu


# Create your views here.
def public_menu_list(request)