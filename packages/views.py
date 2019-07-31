from django.shortcuts import render
from .models import Packages
from .services import dest_object_to_dict
from django import template


# Create your views here.

def home(request):
	data_for_home_page = {}
	data_for_home_page['is_logged_in'] = False

	dests_object_list = Packages.objects.all()
	dests_dict_list = []

	if 'username' in request.session:
		data_for_home_page['is_logged_in'] = True
	for dest in dests_object_list:
		dest_dict = dest_object_to_dict(dest)
		dests_dict_list.append(dest_dict)
	data_for_home_page['dests'] = dests_dict_list
	return render(request, 'home.html', {'data_for_home_page': data_for_home_page})


def package_info(request, _id):
	dest_object = Packages.objects.get(id=_id)	
	dest_in_dict = dest_object_to_dict(dest_object)
	return render(request, "package_info.html", {'dest_info':dest_in_dict})
