from django.shortcuts import render
from .models import Question, Answer, Comments
from .services import get_answers_of_question
# Create your views here.

def home(request):
	user_dict = {}
	questions_dict = {}
	if 'username' in request.session:
		username = request.session['username']
		user_dict['user_dict'] = username
	questions = Question.objects.all()
	for question in questions:
		question_dict = {}
		question_dict['question'] = question.question
		question_dict['answers'] = get_answers_of_question(question.id)

		questions_dict[question.id] = question_dict

	return render(
		request, 'forum_home.html', {
		'user': user_dict,
		'questions': questions_dict
		})

def submit_question(request):
	pass