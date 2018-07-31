from django.contrib import admin

# Register your models here.
from .models import (Question, Choice)

# class QuestionAdmin(admin.ModelAdmin):
# 	# fields = ['pub_date', 'question_text']
# 	fieldsets = [
# 		(None, {'fields': ['question_text']}),
# 		('Date information', {'fields': ['pub_date']})
# 	]
# admin.site.register(Question, QuestionAdmin)
# class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 3

class QuestionAdmin(admin.ModelAdmin):
	list_display	=	('question_text',	'pub_date', 'was_published_recently')
	fieldsets = [
	(None, {'fields': ['question_text']}),
	('Date information', {'fields':['pub_date'], 'classes': ['collapse']}),
	]
	inlines = [ChoiceInline]
	#gives a filter sidebar in the  Question admin section
	list_filter = ['pub_date']
	#gives a search bar in the  Questionadmin section
	search_fields = ['question_text']

admin.site.register(Choice)
admin.site.register(Question, QuestionAdmin)