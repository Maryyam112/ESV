from django.urls import path
from esv.views import movie
from django.urls import path, include
urlpatterns = [
    path('', movie),

]