# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
import MySQLdb
from ujourney.models import Article, Users
from django.template.loader import get_template
from django.template import Context
import datetime
from django.template import Template, Context
from ujourney.views import *
# Level 1.0


def level1(request):
	now = Article.objects.all()
	t = get_template('level1/article_list.html')
	html = t.render(Context({'view_article': now}))
	return HttpResponse(html)

def view_article(request):
	now = Article.objects.all()
	t = get_template('level1/article_list.html')
	html = t.render(Context({'view_article': now}))
	return HttpResponse(html)

def user_profile(request):
	usp = Users.objects.all()
	t = get_template('level1/profile.html')
	html = t.render(Context({'user_profile': usp}))
	return HttpResponse(html)
	#profile.html

def add_article(request):
	if 'foo' in request.POST:
		add = Article.objects.create(article=request.POST['foo'], date=datetime.datetime.now())
		add.save()
		return HttpResponseRedirect("/articles/")
	else:
		return render_to_response('level1/add_article.html')

