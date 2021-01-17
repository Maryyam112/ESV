
from django.contrib import admin
from django.urls import path
from helpModule.views import help
from helpModule import views

urlpatterns = [
    path('', help),
    path('help', views.help),
    path('about',views.aboutPage),

]
