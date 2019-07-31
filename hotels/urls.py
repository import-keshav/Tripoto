from django.urls import path
from . import views

urlpatterns = [
	path('', views.hotel_home_page, name='hotel_home_page')
]