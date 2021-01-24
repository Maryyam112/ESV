from django.core.mail import send_mail
from django.shortcuts import render
from django.shortcuts import HttpResponse


def help(request):
    return render(request , 'help.html')

def aboutPage(request):
    return render(request , 'aboutus.html')

def profile(request):
    # check user is authenticated or not
    if request.user.is_authenticated:
        return render(request , 'profile.html')
    else
        return redirect('login.html')

def contact(request):
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message_phone = request.POST['message-phone']
        message = request.POST['message']
        return render(request, 'contact.html', {'msgname': message_name})

        #send an email
        send_mail(
            message_name,
            message,
            message_email,
            ['maryamahsan@gamil.com'],
            message_phone,
        )
    else:
        return render(request , 'contact.html', {})


