# -*- coding: utf-8 -*-
import md5
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
import MySQLdb
from ujourney.models import Users
from django.template.loader import get_template
from django.template import Context

def registration_save(request):
	if 'first_name' in request.POST:
		man = request.POST['first_name']
		t = get_template('level0/email_sender.html')
		message = t.render(Context({'first_name': man}))
		savebase = Users(login=request.POST['login'],first_name=request.POST['first_name'],second_name=request.POST['second_name'],email=request.POST['email'], passwd=gen_pas(request.POST['passwd']), sex=request.POST['sex'],)
		savebase.save()
	else:
		man = 'username'
		t = get_template('level0/email_sender.html')
		message = t.render(Context({'first_name': man}))
	return HttpResponse(message)
	
def registration(request):
	if request.method == 'POST':
		form = AddMessage(request.POST)
		if form.is_valid():
			login = form.cleaned_data['login']
			first_name = form.cleaned_data['first_name']
			second_name = form.cleaned_data['second_name']
			email = form.cleaned_data['email']
			passwd = form.cleaned_data['passwd']
			sex = form.cleaned_data['sex']			
		return render_to_response('index.html')
	else:
		return render_to_response('level0/registration.html')
		
		
def rules_of_the_game(request):
	return render_to_response('level0/rules_of_the_game.html')

def user_agreement(request):
	return render_to_response('level0/user_agreement.html')

def gen_pas(pasw):
    pwd = md5.new()
    pwd.update(pasw)
    return pwd