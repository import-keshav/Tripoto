from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home'),
	path('submit_question', views.submit_question, name='submit_question')
]