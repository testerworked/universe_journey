# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render_to_response
import MySQLdb
from ujourney.models import Users
from ujourney.level0 import gen_pas

def main(request):
	return render_to_response('index.html')
	
def login(request):
    try:
        m = Users.objects.get(login=request.POST['login'])
        if m.passwd == request.POST['password']:
            request.session['member_id'] = m.id
            #return HttpResponse("You login it - %s" % request.session['member_id'])
            return render_to_response('level1/tabs/index.htm')
    except Users.DoesNotExist:
        return HttpResponse("Sorry, repeat please!")

def logout(request):
    try:
        del request.session['member_id']
    except KeyError:
        pass
    return HttpResponse("You're out.")
