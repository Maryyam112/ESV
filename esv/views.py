from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.template import RequestContext

def signupsignin(request):
    return render(request, 'registration.html')
def home(request):
    return render(request, 'index.html')
def handleSignup(request):
    if request.method == 'POST':
       username  = request.POST['username']
       password1 = request.POST['password1']
       password2 = request.POST['password2']
       email = request.POST['email']
       if password1 != password2:
           messages.error(request, "Password do not match")
           return redirect('home')
       myuser = User.objects.create_user(username=request.POST.get('username'), email=request.POST.get('email'), password =request.POST.get('password1'))
       myuser.save()
       messages.success(request, "Your account has been successfully created")
       return render(request, 'registration.html')
    else:
        return HttpResponse('404 - Not Found')

def handleLogin(request):
    if request.method == 'POST':
          loginuser = request.POST['loginuser']
          loginpass = request.POST['loginpass']
          user = authenticate(username=loginuser, password=loginpass)
          if user is not None:
              login(request, user)
              messages.success(request, "Successfully Logged In")
              return redirect('home')

          else:
              messages.error(request, "Invalid  Credentials, Please try again")
              return redirect('signupsignin')

          return HttpResponse('handleLogin')


