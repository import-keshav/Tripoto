from django.db import models

# Create your models here.

class Packages(models.Model):
	name = models.CharField(max_length=100)
	img = models.ImageField(upload_to='pics')
	desc = models.TextField()
	hotel_name = models.TextField()
	price = models.IntegerField()
	services = models.TextField()
	day_wise_desc = models.TextField()
	days = models.IntegerField()
	nights = models.IntegerField()
