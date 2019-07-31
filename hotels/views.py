from django.shortcuts import render
from .models import Hotels

# Create your views here.

def hotel_home_page(request):
	return render(request, "hotel.html")

def hotels_at_place(request, place):

	hotels = Hotels.objects.filter(country=place)
	return render(request, "hotels_at_places.html", {'hotels': hotels, 'place': place})