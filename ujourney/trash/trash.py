#views.py
# -*- coding: utf-8 -*-
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render_to_response
from ujourney.forms import ContactForm, AddMessage
from django.views.decorators.csrf import csrf_protect
from django.core.mail import send_mail
import datetime, MySQLdb
from django.db import connection
from django.template import loader, Context


def current_datetime(request):
	now = datetime.datetime.now()
	html = "<html><body>It is now %s.</body></html>" % now
	return HttpResponse(html)
	
def hours_ahead(request, offset):
	try:
		offset = int(offset)
	except ValueError:
		raise Http404()
	dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
	#assert False
	html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
	return HttpResponse(html)
	
def display_meta(request):
	values = request.META.items()
	values.sort()
	html = []
	for k, v in values:
		html.append('<tr><td>%s</td><td>%s</td></tr>' % (k,v))
	return HttpResponse('<table>%s</table>' % '\n'.join(html))
	
def search_form(request):
	return render_to_response('base.html')

def search(request):
	if 'q' in request.GET:
		message = 'you search in: %r' % request.GET['q']
	else:
		message = 'you send a blank message.'
	return HttpResponse(message)
	
def blog_form(request):
	return render_to_response('blog.html')
	
def blog(request):
	if 'message' in request.GET and request.GET['message']:
		message = 'add: %r' % request.GET['message']
		return HttpResponse(message)
	else:
		return HttpResponse('Write you message')

def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			topic = form.cleaned_data['topic']
			message = form.cleaned_data['message']
			sender = form.cleaned_data.get('sender', 'noreply@example.com')
			#send_mail(
            #    'Feedback from your site, topic: %s' % topic,
            #    message, sender,
            #    ['administrator@example.com']
            #)
			return render_to_response('out.html', { 'form':form })
			#return HttpResponseRedirect('/contact/thanks/')
	else:
		form = ContactForm(
			initial={'topic':'I really like your site!'}
		)
	return render_to_response('forms.html', { 'form':form })
	
def my_list(request):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM tester")
    out_rows = cursor.fetchall()
    tt = loader.get_template("archive.html")
    cc = Context({ 'out_rows':out_rows })
    return HttpResponse(tt.render(cc))
	
	
#forms.py

class PersonForm(forms.Form):
	first = forms.CharField(max_length=100, required=True)
	last = forms.CharField(max_length=100, required=True, initial='Smith')
	middle = forms.CharField(max_length=100)
	
class ContactForm(forms.Form):
	topic = forms.CharField(max_length=100)
	message = forms.CharField(widget=forms.Textarea)
	#sender = forms.EmailField(required=False, label="E-mail adress")
	
	def clean_message(self):
		message = self.cleaned_data['message']
		num_words = len(message.split())
		if num_words < 4:
			raise forms.ValidationError('Not enough words!')
		return message
