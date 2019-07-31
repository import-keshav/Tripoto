from .models import Question, Answer, Comments


def get_comments_of_answer(answer_id):
	comments_dict = {}
	comments = Comments.objects.filter(answer_id=answer_id)
	for comment in comments:
		comments_dict[comment.id] = comment.comment

	return comments_dict

def get_answers_of_question(question_id):
	answers_dict = {}
	answers = Answer.objects.filter(question_id=question_id)
	for answer in answers:
		answer_dict = {}
		answer_dict['answer'] = answer.answer
		answer_dict['upvotes'] = answer.upvotes
		answer_dict['comments'] = get_comments_of_answer(answer.id)
		answers_dict[answer.id] = answer_dict

	return answers_dict
