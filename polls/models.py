import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import (
	BaseUserManager , AbstractBaseUser
)

# Create your models here.
class Question(models.Model):
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
	def __str__(self):
		return self.question_text

	def was_published_recently(self):
		now = timezone.now()
		return now - datetime.timedelta(days=1) <= self.pub_date <= now
		was_published_recently.admin_order_field = 'pub_date'
		was_published_recently.boolean = True
		was_published_recently.short_description = 'published recently ?'
		# return self.pub_date >= (timezone.now() - datetime.timedelta(days=1))

class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)
	def __str__(self):
		return self.choice_text

# class Members(models.Model,BaseUserManager):
# 	username =  models.CharField(max_length = 50)
# 	first_name = models.CharField(max_length = 50)
# 	last_name = models.CharField(max_length = 50)
# 	email = models.CharField(max_length = 50)
# 	password = models.CharField(max_length=200)
# 	date_registered = models.DateTimeField('date_registered')
# 	# assoc = models.ManyToManyField()
# 	def __str__(self):
# 		return 	self.username +"  "+ self.last_name 
# 	def get_username(self):
# 		return self.username
# 	def get_names(self):
# 		return self.last_name + " "+ self.first_name
# 	def create_user(self,username,first_name,last_name,email,date_registered,password=None):
# 		#creates and saves a user with a given username, email and password
# 		if not email:
# 			raise ValueError('Users must have email address')
# 		member = self.model(
# 			email = self.normalize(email),
# 			username = username,
# 			# username = self.get_by_natural_key(username),
# 			# def clean(self):
# 			# 	username = get_by_natural_key(),
# 			first_name = first_name,
# 			last_name = last_name,
# 			date_registered = date_registered,
# 		)
# 		member.set_password(password)
# 		member.save(using = self._db )
# # class MyUserManager(BaseUserManager):
# # 	def create_user(self, username,email,password=None):
# # 		#creates and savesa a user with a given username,email and password
# # 		if not email:
# # 			raise ValueError('Users must have a valid email address')
# # 		user = self.model(
# # 			email = self.normalize_email(email),
# # 			username = username,
# # 		)
# # 		user.set_password(password)
# # 		user.def save(self, using):
# # 				using = self._db
# # 			 super(MyUserManager, self).save(using) # Call the real save() method
# # 		return user
# class MyMember(AbstractBaseUser):
# 		email = models.EmailField(
# 		 verbose_name= " email address",
# 		 max_length=254,
# 		 unique = True,
# 		)
# 		username = models.CharField(max_length=50)
# 		first_name = models.CharField(max_length = 100)
# 		last_name = models.CharField(max_length= 100)
# 		date_registered = models.DateTimeField()
# 		is_active = models.BooleanField(default = True)
# 		is_admin = models.BooleanField(default = False)
		
# 		objects = Members()
# 		USERNAME_FIELD = 'username'
# 		REQUIRED_FIELD = ['first_name','last_name','email']		
# 		def __str__(self):
# 				return self.username

# 		def has_perm(self, perm, obj=None):
# 		#Does the user/Member Have a specific permission?
# 		#simplest possible answer is yes, always(superuser) || but in this case no.		
# 				return False
		
# 		def has_module_perms(self, app_label):
# 		#does the user have permission to view the app 'app-label?'
# 		#Simplest Possible answer is yes ,(if superUser) || but in this case No	
# 			return False
		
# 		@property
# 		def is_staff(self):
# 			return False