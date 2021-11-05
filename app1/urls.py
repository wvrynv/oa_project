from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('career/', views.career, name='career'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('team/', views.team, name='team'),
    path('projects/', views.projects, name='projects'),
]