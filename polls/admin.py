from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
# Register your models here.
from .models import (Question, Choice, Members)
# from customauth.models import MyMember

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

# class UserCreationForm(forms.ModelForm):
# 		# a form for creating users, including all required fields, plus a repeated password
# 		password1 = forms.CharField(label='Password', widget = forms.PasswordInput)
# 		password2 = forms.CharField(label = 'Password confirmation', widget = forms.PasswordInput)

# 		class Meta:
# 			model = MyMember
# 			fields = ('email','username','first_name','last_name','date_registered')
		
# 		def clean_password(self):
# 			#to check if the two password Match
# 			pasword1 = self.cleaned_data.get('password1')
# 			password2 = self.cleaned_data.get('password2')

# 			if password1 and password2 and password1 != password2 :
# 				raise forms.ValidationError('Password MisMatch')
# 			return password2 
		
# 		def save(self, commit = True)
# 			#save the provided password in a hash format
# 			member = super().save(commit = False)
# 			member.set_password(self.cleaned_data['password1'])
# 			if commit:
# 				user.save()
# 			return user

# class UserAdmin(BaseUserAdmin):
	

admin.site.register(Choice)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Members)
# admin.site.register(MyMember, UserAdmin)