"""emotion URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin

from django.urls import path
from esv import views
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.signupsignin, name='signupsignin'),
    path('index.html', views.home, name='home'),
    path('video.html', views.movie, name='movie'),
    path('signup', views.handleSignup, name='handleSignup'),
    path('login', views.handleLogin, name='handleLogin'),
    path('contact.html', views.contact,name='contact'),
    path('feedback_submit', views.feedback_submit, name = 'feedback_submit'),
    path('', include('esv.urls')),
    path('contact.html', views.contact),
    path('logout.html', views.logout, name='logout'),
    path('help.html', views.help),
    path('aboutus.html',views.aboutPage),
]+ static(settings.MEDIA_URL, document__root=settings.MEDIA_ROOT)
