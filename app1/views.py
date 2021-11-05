from django.conf.urls import url
from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import message, send_mail
import win32com.client as win32  

# Create your views here.

def index (request):
    return render(request, 'app1/index.html', {})

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
            message_email, #from email
            ["marina.samoilenko6@gmail.com"], #to email(s)
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


