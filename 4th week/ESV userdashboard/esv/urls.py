from django.urls import path
from esv.views import movie
from . import views
urlpatterns = [
    path('', movie),

]