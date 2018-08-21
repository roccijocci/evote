from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import admin
from django.template import loader

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
# from django.template import loader
from .models import Question, Choice , Members 

# class AdminView(LoginRequiredMixin,generic.ListView):
# 	template_name = 'admin/'
# 	login_url = '../account/login'
# 	redirect_field_name = 'redirect_to'

class IndexView(LoginRequiredMixin,generic.ListView):
	template_name = 'polls/index.html'
	# template_name = 'admin/'
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
	
def members(request):
	members_names = Members.objects.order_by('id')[:10]
	context = {'members_names': members_names}
	return render(request, 'polls/members.html', context)
	
	# return HttpResponse("You are voting on question %s." % question_id)
# class MemberDetailView(generic.DetailView):
# 	model =  Members
# 	template = 'polls/members.html'
# 	context_object_name = 'members_name'

# def members(request, member_id):
# 	members	= get_object_or_404(Members,pk=member_id)
# 	context = {'members_name': members_name}
# 	return render(request, 'polls/members.html',context)
# class DetailView(DetailView):
# 		model = Members
# 		template_name='polls/members.html'
# 		context_object_name = 'members'

# def members(request):
#  members_name	= get_object_or_404(Members)
#  context = members_name.
#  return render(request, 'polls/members.html','members':get_names())
# 	# members = Members.object.get(pk=member_id)

# def members(request):
# 	members_names = Members.objects.order_by('id')[:10]
# 	output = ','.join([m.first_name for m in members_names]) 
# 	return HttpResponse(output)


# def members(request):
# 	members_names = Members.objects.order_by('id')[:10]
# 	template = loader.get_template('polls/members.html')
# 	context = {
# 		'members_names':members_names,
# 	}
# 	return HttpResponse(template.render(context,request))