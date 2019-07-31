from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name="home"),
	path('package_info/<int:_id>', views.package_info, name="package_info"),
]