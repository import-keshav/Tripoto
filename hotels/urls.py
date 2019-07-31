from django.urls import path
from . import views

urlpatterns = [
	path('home', views.hotel_home_page, name='home'),
	path('at_places/<str:place>', views.hotels_at_place, name='places')
]