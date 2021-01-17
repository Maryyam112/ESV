
from django.shortcuts import render
from django.shortcuts import HttpResponse


def help(request):
    return render(request , 'help.html')

def aboutPage(request):
    return render(request , 'aboutus.html')

