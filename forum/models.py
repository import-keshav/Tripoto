from django.db import models

# Create your models here.

class Question(models.Model):
	question = models.TextField()

class Answer(models.Model):
	question_id = models.IntegerField()
	answer = models.TextField()
	upvotes =  models.IntegerField()

class Comments(models.Model):
	answer_id = models.IntegerField()
	comment = models.TextField()
