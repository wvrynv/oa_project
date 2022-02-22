from django.conf import settings
from django.conf.urls import url
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import message, send_mail
from django.shortcuts import render
import datetime
from django.utils import translation


# Create your views here.

def index(request):
    context = {
        "cookie": request.COOKIES.get("lang", '')
    }
    print(request.COOKIES.get("lang"))
    response = render(request, 'app1/index.html', context)
    if not request.COOKIES.get('lang'):
        set_cookies(request, response)
    return response


def set_cookies(request, response):
    current_lang = translation.get_language()

    max_age = 7 * 24 * 60 * 60  # one week 
    expires = datetime.datetime.utcnow() + datetime.timedelta(seconds=max_age)
    response.set_cookie('lang', request.GET.get("lang", current_lang),
                expires=expires.utctimetuple(), max_age=max_age)


def delete_cookiee(request):
    response = render(request, '/')
    delete_cookies(request, response)
    return response

def delete_cookies(request, response):
    response.set_cookie(request.GET.get("lang",''), expires=0, max_age=0)


def contact_us (request):
    
    if request.method == "POST":

        message_name = request.POST.get('message_name')
        message_phone = request.POST.get('message_phone')
        message_email = request.POST.get('message_email')
        message = request.POST.get('message')


        text = "Name: {} \nPhone: {} \nEmail: {} \nMessage: {}".format(message_name, message_phone, message_email, message)

        send_mail(
            "Message from web-site, from " + message_name, #subject
            text, #message
            "olivkaadvisory@gmail.com", #from email
            ["m.samoilenko@oliva-advisory.de"], #to email(s)
        )
        
        return render(request, 'app1/contact_us.html', {'message_name': message_name})
    else:
        return render(request, 'app1/contact_us.html', {})

def projects (request):
    return render(request, 'app1/projects.html')

def career (request):
    return render(request, 'app1/career.html')

def team (request):
    return render(request, 'app1/team.html')

def change_status_career(request):
    return render(request, 'app1/team.html')

def imprint(request):
    return render(request, 'app1/imprint.html')

def privacy_policy(request):
    return render(request, 'app1/privacy_policy.html')
