from django.db import models

class Users(models.Model):
	login = models.CharField(max_length=30)
	first_name = models.CharField(max_length=30)
	second_name = models.CharField(max_length=30)
	email = models.EmailField(max_length=30)
	passwd = models.CharField(max_length=180)
	sex = models.BooleanField()
	
	def __unicode__(self):
		return self.short_name
