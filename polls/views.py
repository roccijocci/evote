from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
# from django.template import loader
from .models import Question, Choice  


class IndexView(LoginRequiredMixin,generic.ListView):
	template_name = 'polls/index.html'
	context_object_name = 'latest_question_list'
	login_url = '../account/login'
	redirect_field_name = 'redirect_to'

	def get_queryset(self):
		# Return the last five published questions
		# return Question.objects.order_by('-pub_date')[:5]
		return Question.objects.filter(
			pub_date__lte = timezone.now()
		).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
	model = Question
	template = 'polls/detail.html'

# class ResultsView(generic.DetailView):
# 	model = Question
# 	template = 'polls/results.html'

# def vote(request, question_id):
# 	question = get_object_or_404(Question, pk=question_id)
# 	try:
# 		selected_choice = question.choice_set.get(pk = request.POST['choice'])
# 	except (KeyError, Choice.DoesNotExist):
# 		#redisplay the question vting form.
# 		return render(request, 'polls/detail.html',{'question':question,'error_message': "You did not select a choice.",})
# 	else:
# 		selected_choice.votes += 1
# 		selected_choice.save()
# 		return HttpResponseRedirect(reverse('polls:results', args = (question_id,)))
# 		return HttpResponse("You are voting on question %s." % question_id)



# def index(request):
# 	latest_question_list = Question.objects.order_by('-pub_date')[:5]
# 	context = {'latest_question_list': latest_question_list}
# 	return render(request, 'polls/index.html', context)
# 	# template = loader.get_template('polls/index.html')
# 	# context = {
# 	# 	'latest_question_list': latest_question_list,
# 	# }
# 	# return HttpResponse(template.render(context,request))
# 	# output = ', '.join([q.question_text for q in latest_question_list])
# 	# return HttpResponse(output)
# 	#return HttpResponse("Hello, world. You are at the polls index.")

# def detail(request, question_id):
# 	question = get_object_or_404(Question, pk=question_id)
# 	return render(request, 'polls/detail.html',	{'question':question})
# 	# return HttpResponse("You are looking at the results of a question %s." % question_id)
# 	# try:
# 	# 	question = Question.objects.get(pk = question_id)
# 	# except Question.DoesNotExist:
# 	# 	raise Http404("Question Does not Exist")
# 	# return render(request, 'polls/detail.html', {'question':question})
def results(request, question_id):
	# response = "You are looking at the results of question %s."
	# return HttpResponse(response % question_id)
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/results.html', {'question': question})

def get_queryset(self):
	#excludes any questions that are not published yet
	return Question.objects.filter(pub_date__lte = timezone.now())

def vote(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = question.choice_set.get(pk = request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		#redisplay the question vting form.
		return render(request, 'polls/detail.html',{'question':question,'error_message': "You did not select a choice.",})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		return HttpResponseRedirect(reverse('polls:results', args = (question_id,)))
	# return HttpResponse("You are voting on question %s." % question_id)
