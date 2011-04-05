# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render_to_response
import MySQLdb
from ujourney.models import Users

def level_0(request):
	return render_to_response('index.html')

def post_comment(request, new_comment):
    if request.session.get('has_commented', False):
        return HttpResponse("Вы уже отправили комментарий")
    c = comments.Comment(comment=new_comment)
    c.save()
    request.session['has_commented'] = True
    return HttpResponse('Спасибо за ваш комментарий!')

def login(request):
    try:
        m = Member.objects.get(username__exact=request.POST['username'])
        if m.password == request.POST['password']:
            request.session['member_id'] = m.id
            return HttpResponse("Вы авторизованы.")
    except Member.DoesNotExist:
        return HttpResponse("Ваши логин и пароль не соответствуют.")

def logout(request):
    try:
        del request.session['member_id']
    except KeyError:
        pass
    return HttpResponse("Вы вышли.")

def login(request):

    # Если мы отправили форму...
    if request.method == 'POST':

        # Проверить, что браузер принимает cookie:
        if request.session.test_cookie_worked():

            # Браузер принимает, удаляем тестовый cookie.
            request.session.delete_test_cookie()

            # На практике нам потребуется некая логика для проверки
            # логина и пароля, но так как это всего лишь пример...
            return HttpResponse("You're logged in.")

        # Проверка не прошла, отображаем сообщение об ошибке.
        # На настоящем сайте нам потребуется отображать это покрасивее.
        else:
            return HttpResponse("Please enable cookies and try again.")

    # Если мы не отсылали форму, отправляем тестовое cookie
    # вместе с формой аутентификации.
    request.session.set_test_cookie()
    return render_to_response('foo/login_form.html')

	