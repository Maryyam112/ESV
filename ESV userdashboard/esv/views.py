from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from esv.models import Feedback
from esv.models import Video
from esv.models import Item


from django.template import RequestContext

def movie(request):
    obj=Item.objects.all()
    return render(request, 'video.html', {'obj':obj})

def contact(request):
    return render(request, 'contact.html')
def feedback_submit(request):
    name = request.POST["name"]

    comment = request.POST["comment"]

    submit = Feedback(name=name, comment=comment)
    submit.save()

    return render(request, 'contact.html')

def signupsignin(request):
    return render(request, 'registration.html')
def home(request):
    videos = Video.objects.all()

    return render(request, 'index.html', {'videos': videos})
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


