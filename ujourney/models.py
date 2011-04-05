from django.db import models
from django.contrib.auth.models import User, UserManager


class Users(models.Model):
	login = models.CharField(max_length=30)
	first_name = models.CharField(max_length=30)
	second_name = models.CharField(max_length=30)
	email = models.EmailField(max_length=30)
	passwd = models.CharField(max_length=180)
	sex = models.BooleanField()

	def __unicode__(self):
		return self.login

class Article(models.Model):
	user = models.OneToOneField(Users, related_name='app_profile', primary_key=True)
	article = models.TextField()
	date = models.DateField()

	def __unicode__(self):
		return self.article


class Comments(models.Model):
	user = models.ForeignKey(Users)
	date = models.DateField()
	comment_text = models.TextField()
	article = models.ForeignKey(Article)

	def __unicode__(self):
		return self.comment_text

class CustomUser(User):
	timezone = models.CharField(max_length=50, default='Europe/London')
	