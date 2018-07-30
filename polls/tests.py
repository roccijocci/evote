import datetime
from django.test import TestCase
from django.utils import timezone

from .models import Question
# Create your tests here.

class QuestionModelTest(TestCase):
	# was_published_recently returns true forquestions whose pub_date is in the future
	#it should return false for pub_date set in the future.

	time = timezone.now() + datetime.timedelta(days=30)
	future_question = Question(pub_date=time)
	self.assertIs(future_question.was_published_recently(), false)