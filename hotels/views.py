from django.shortcuts import render

# Create your views here.

def hotel_home_page(request):
	return render(request, "hotel.html")