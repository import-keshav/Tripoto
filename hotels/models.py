from django.db import models

# Create your models here.

class Hotels(models.Model):
	name = models.CharField(max_length=100)
	continent = models.CharField(max_length=50)
	country = models.CharField(max_length=50)
	state = models.CharField(max_length=50)
	city = models.CharField(max_length=50)
	price = models.IntegerField()
	image = models.ImageField(upload_to='pics')