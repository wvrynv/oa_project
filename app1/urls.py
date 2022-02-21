from xml.dom.minidom import Document
from django.urls import path
from django.contrib import admin
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('career/', views.career, name='career'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('team/', views.team, name='team'),
    path('projects/', views.projects, name='projects'),
    path('imprint/', views.imprint, name='imprint'),
    path('privacy_policy/', views.privacy_policy, name='privacy_policy'),
]
