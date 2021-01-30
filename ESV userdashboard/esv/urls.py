from django.urls import path
from esv.views import movie
urlpatterns = [
    path('', movie),
]