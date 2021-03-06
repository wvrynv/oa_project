from curses.ascii import HT
from django.conf import settings
from django.conf.urls import url
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import message, send_mail
from django.shortcuts import render
import datetime
from django.utils import translation
from django.contrib import messages
# Create your views here.

def index(request):
    context = {
        "cookie": request.COOKIES.get("lang")
    }
    response = render(request, 'app1/index.html', context)
    if not request.COOKIES.get('lang'):
        set_cookies(request, response)
    return response


def set_cookies(request, response):
    current_lang = translation.get_language()

    max_age = 180  # one week
    expires = datetime.datetime.utcnow() + datetime.timedelta(seconds=max_age)
    response.set_cookie('lang', request.GET.get("lang", current_lang),
                expires=expires.utctimetuple(), max_age=max_age)


# def delete_cookiee(request):
#     response = render(request, '/')
#     delete_cookies(request, response)
#     return response
#
# # cookie func
# def delete_cookies(request, response):
#     response.set_cookie(request.GET.get("lang",''), expires=0, max_age=0)

from django.http import HttpResponseRedirect

def delete(request):
    response = render(request, 'app1/index.html')
    delete_cookie(request, response)
    return HttpResponseRedirect(request.path_info)


def delete_cookie(request, response):
    response.set_cookie(max_age=0, expires='Thu, 01-Jan-1970 00:00:00 GMT')


def contact_us(request):
    
    if request.method == "POST":
        message_name = request.POST.get('message_name')
        message_phone = request.POST.get('message_phone')
        message_email = request.POST.get('message_email')
        message = request.POST.get('message')

        
        text = "Name: {} \nPhone: {} \nEmail: {} \nMessage: {}".format(message_name, message_phone, message_email, message)

        send_mail(
            "Message from web-site, from " + message_name, #subject
            text, #message
            settings.EMAIL_HOST_USER, #from email
            (message_email,) #to email(s)
        )
        messages.success(request, "Message has successfully been sent !")
        context = {
            'message_name': message_name,
            "cookie": request.COOKIES.get("lang"),
            "messages": messages
        }
        return render(request, 'app1/contact_us.html', context)
    else:
        messages.success(request, "Message has successfully been sent !")
        context = {
            "cookie": request.COOKIES.get("lang"),
            "messages": messages
        }
        return render(request, 'app1/contact_us.html', context)


def projects (request):
    context = {
        "cookie": request.COOKIES.get("lang")
    }
    return render(request, 'app1/projects.html', context)


def career(request):
    context = {
        "cookie": request.COOKIES.get("lang")
    }
    return render(request, 'app1/career.html', context)


def team(request):
    context = {
        "cookie": request.COOKIES.get("lang")
    }
    return render(request, 'app1/team.html', context)


def change_status_career(request):
    return render(request, 'app1/team.html')


def imprint(request):
    return render(request, 'app1/imprint.html')


def privacy_policy(request):
    return render(request, 'app1/privacy_policy.html')
