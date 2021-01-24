
from django.contrib import admin
from django.urls import path
from helpModule.views import help
from helpModule import views

urlpatterns = [
    path('', help),
    path('help.html', views.help, name="help"),
    path('about.html',views.aboutPage, name="about"),
    path('contact.html',views.contact, name="contact"),
    path('profile.html',views.contact, name="profile"),


]
